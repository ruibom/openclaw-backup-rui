# LinkedIn Post Analytics — Full System Blueprint

**Version:** March 2026  
**Owner:** Rui Bom  
**Maintained by:** Apex agent  
**Purpose:** This document describes the complete end-to-end system for collecting LinkedIn post stats, deriving insights, and feeding those insights back into Rui's content strategy.

---

## 1. SYSTEM OVERVIEW

```
LinkedIn Profile
      │
      ▼
[Apify Scraper]  ←────── triggered by Apex (cron or manual)
      │
      ▼
linkedin-post-analytics.py  ←── ~/.openclaw/tools/linkedin-post-analytics.py
      │
      ├── Analyze post metadata (hook, topic, format, CTA, word count, day)
      ├── Score performance tier (Viral / Strong / Average / Weak)
      └── Deduplicate against Notion DB
              │
              ▼
      [Notion DB: LinkedIn Post Analytics]
      DB ID: 3154affb-d00c-814e-bc1a-d0d9072aad24
      URL: https://www.notion.so/3154affbd00c814ebc1ad0d9072aad24
              │
              ▼
      Apex cron: apex-linkedin-analytics (20:00 JST daily)
              │
              ├── Diagnose underperformers (<20 likes)
              ├── Research competitor viral posts
              ├── Pattern analysis across all DB entries
              └── Post insights + 2-3 post recommendations to #apex-career
                              │
                              ▼
                    LINKEDIN_VOICE.md ← updated with proven formulas
```

---

## 2. DATA COLLECTION: APIFY SCRAPER

### Actor
- **ID:** `harvestapi~linkedin-profile-posts`
- **Endpoint:** `https://api.apify.com/v2/acts/harvestapi~linkedin-profile-posts/run-sync-get-dataset-items?token={APIFY_TOKEN}`
- **Profile scraped:** `https://www.linkedin.com/in/rui-bom`

### Input payload
```json
{
  "targetUrls": ["https://www.linkedin.com/in/rui-bom"],
  "maxPosts": 10,
  "postedLimit": "week",
  "includeQuotePosts": true,
  "includeReposts": false,
  "scrapeComments": true,
  "maxComments": 10,
  "scrapeReactions": false
}
```

### Output fields used
| Apify Field | Maps to Notion Property |
|---|---|
| `content` | Content Summary, Hook Line, Word Count |
| `engagement.likes` | Likes |
| `engagement.comments` | Comments |
| `engagement.shares` | Reposts |
| `linkedinUrl` | LinkedIn URL (dedup key) |
| `postedAt.date` | Date Posted, Day of Week |
| `postImages[]` | Format detection |
| `document.totalPageCount` | Format detection (Carousel) |
| `comments[]` | Top Comments |

### Run command (manual)
```bash
cd ~/.openclaw/workspace/agents/apex
python3 ~/.openclaw/tools/linkedin-post-analytics.py week 10
# Args: [posted_limit] [max_posts]
# posted_limit: "1h" | "24h" | "week" | "month"
# max_posts: integer
```

### Credentials location
- `APIFY_TOKEN` → `~/.openclaw/workspace/.env`
- `NOTION_API_KEY` → `~/.openclaw/workspace/.env` + `~/.zshrc`

---

## 3. DATA ANALYSIS: WHAT THE SCRIPT COMPUTES

### 3a. Topic Classification
Auto-detected by keyword matching against post content:

| Topic | Keywords that trigger it |
|---|---|
| AI/Tech | ai, automation, gpt, llm, saas, software |
| Leadership | leader, culture, hire, ceo, founder |
| Revenue/GTM | revenue, sales, gtm, pipeline, arr, deal |
| Career | career, job, interview, linkedin, hired |
| Personal Story | "i remember", "years ago", "my story" |
| Hot Take | "unpopular opinion", "hot take", "nobody talks about" |
| Framework/Playbook | framework, playbook, "step 1", "here's how" |
| Industry Insight | market, trend, prediction, disruption |

### 3b. Hook Type Classification
Detected from the first line of the post:

| Hook Type | Detection Rule |
|---|---|
| Contrarian | "wrong", "stop", "nobody", "controversial", "myth" |
| Question | Ends with `?` |
| Story | Starts with "I", "My", "When I", "Years ago" |
| Stat/Data | Contains `%`, "billion", "million", "data", "research" |
| List/Framework | "here's", "how to", "ways to", "steps" |
| Personal Confession | "confess", "admit", "honest", "truth", "secret" |
| Bold Claim | Default if none of the above match |

### 3c. Format Detection
| Format | Detection Logic |
|---|---|
| Carousel | `document.totalPageCount > 1` |
| Document | `document` field exists, single page |
| Text + Image | `postImages[]` is non-empty |
| Text Only | No images or document |

### 3d. CTA Detection
Detected from last 3 lines of post:
- **Question** → `?` in last 3 lines
- **Follow me** → "follow" or "connect"
- **Repost** → "repost" or "share"
- **Link** → "link", "http", "lnkd"
- **None** → default

### 3e. Performance Tier
Based on total engagement (likes + comments + reposts):
- **Viral** → 500+
- **Strong** → 100–499
- **Average** → 30–99
- **Weak** → <30

### 3f. Deduplication
Before creating a new Notion entry, the script queries the DB for all existing `LinkedIn URL` values. If a post already exists, it **updates** (PATCH) the stats rather than creating a duplicate. New posts get full **CREATE**.

---

## 4. NOTION DATABASE: SCHEMA

**DB ID:** `3154affb-d00c-814e-bc1a-d0d9072aad24`

| Property | Type | Description |
|---|---|---|
| Post Title | Title | First line / hook (max 100 chars) |
| Date Posted | Date | ISO date from Apify `postedAt` |
| LinkedIn URL | URL | Direct post URL (dedup key) |
| Topic | Select | AI/Tech, Leadership, Revenue/GTM, Career, Personal Story, Hot Take, Framework/Playbook, Industry Insight |
| Format | Select | Text Only, Text + Image, Carousel, Video, Poll, Document, Repost + Commentary |
| Hook Type | Select | Contrarian, Question, Story, Stat/Data, Bold Claim, List/Framework, Personal Confession |
| Likes | Number | Raw like count |
| Comments | Number | Raw comment count |
| Reposts | Number | Raw repost count |
| Impressions | Number | (Manual input — LinkedIn native only) |
| Engagement Rate | Number | (likes+comments+reposts)/impressions, if impressions available |
| Top Comments | Rich Text | First 3 notable comments (name + excerpt) |
| Content Summary | Rich Text | First 300 chars of post |
| Hook Line | Rich Text | Exact first line |
| Word Count | Number | Total word count |
| CTA Type | Select | Question, Follow me, Repost, Link, None |
| Performance | Select | Viral, Strong, Average, Weak |
| Day of Week | Select | Monday–Sunday |
| Insights | Rich Text | Manual or Apex-generated analysis |

**Notion API auth:**
```bash
Authorization: Bearer $NOTION_API_KEY
Notion-Version: 2022-06-28
```

---

## 5. AUTOMATED CRON JOB

### Job: `apex-linkedin-analytics`
- **Schedule:** Every day at **20:00 JST**
- **Agent:** apex
- **Delivery:** #apex-career (channel `1476140537202475008`)

### What it does (5 steps):
1. **Run the scraper:**
   ```bash
   python3 ~/.openclaw/tools/linkedin-post-analytics.py month 50
   ```
   Updates Notion DB with latest stats for last 50 posts.

2. **Diagnose underperformers:**
   For any post with <20 likes, Apex evaluates using the Post Diagnosis Framework:
   - Hook strength (curiosity gap? pattern interrupt? specific enough?)
   - Structure (short paragraphs? white space? narrative arc?)
   - Engagement triggers (invites response? clear CTA? speaks TO reader?)
   - Timing & format (peak hours? right format for content type? 150-300 word count?)

3. **Competitive research:**
   Apex rotates through benchmark creators (see list below) weekly.
   `web_search` for their recent high-performing posts. Analyzes hooks, formats, engagement patterns. Compares against Rui's data.

4. **Pattern analysis:**
   Across all Notion entries, identifies:
   - Best performing **topic** (by avg total engagement)
   - Best **hook type** (by avg total engagement)
   - Best **day of week** (by avg total engagement)
   - Best **format** (by avg total engagement)
   - Best **CTA type** (by avg total engagement)
   - **Word count sweet spot** (word count range of top-performing posts)
   - **Engagement rate trend** (week-over-week)

5. **Recommendations:**
   Apex proposes 2-3 post ideas with:
   - Topic + hook type + format combo
   - Draft hook line
   - Data-backed reasoning (e.g. "Your last 3 Contrarian posts averaged 280 engagement vs 45 for other types")
   - Reference to a competitor post using similar approach

**Output posted to #apex-career** (Discord channel `1476140537202475008`)

---

## 6. POST DIAGNOSIS FRAMEWORK

Used by Apex when analyzing underperforming posts (<20 likes):

### Hook Analysis
- Does the first line create a curiosity gap or pattern interrupt?
- Is it specific enough? (numbers, names, stakes)
- Does it pass the "scroll test" — would you stop scrolling?

### Structure Analysis
- Short paragraphs (1–2 lines max for LinkedIn mobile)?
- Enough white space?
- Uses the "1-1-1" rhythm (one idea per line)?
- Is there a narrative arc (setup → tension → resolution)?

### Engagement Triggers
- Does it invite response? (question, controversial take, relatable pain)
- Is there a clear CTA or does it just trail off?
- Does it speak TO the reader or AT the reader?

### Timing & Format
- Posted during peak hours? (Tue–Thu 7–9AM in target timezone)
- Right format for the content? (story → text, data → carousel, opinion → text)
- Word count sweet spot: 150–300 words for text posts

---

## 7. COMPETITIVE INTELLIGENCE SOURCES

Apex rotates through these creators weekly during the analytics cron:

| Creator | Focus Area | Why Benchmark |
|---|---|---|
| Kyle Coleman (CMO Copy.ai) | Hook mastery, contrarian takes | Best hook writer in GTM space |
| Chris Walker (Passetto) | Data-driven GTM, bold claims | Revenue/GTM authority |
| Sahil Bloom | Storytelling frameworks | Narrative structure mastery |
| Justin Welsh | Solopreneur, systems | Consistent high engagement |
| Lara Acosta | Content strategy, engagement | LinkedIn-native tactics |
| Sam McKenna (#samsales) | Sales leadership, authenticity | Similar audience to Rui |
| Morgan Ingram | Sales, video | Engagement playbooks |
| Dave Gerhardt (Exit Five) | B2B marketing | B2B content expert |
| Josh Braun | Sales methodology | Micro-content mastery |
| Jen Allen-Knuth | Sales leadership, vulnerability | Authentic storytelling |

**Research method:**
```
web_search "[creator name] LinkedIn post viral 2025"
```
Analyze: hook type, format, word count, engagement, topic. Compare against Rui's top performers.

---

## 8. FEEDBACK LOOP: LINKEDIN_VOICE.MD

After each analytics run, proven patterns are written back into:
`~/.openclaw/workspace/agents/apex/LINKEDIN_VOICE.md`

Updates include:
- **Proven hook formulas** with engagement data
- **Topics that resonate** with engagement numbers
- **Formats that work** with comparative data
- **Posting cadence** recommendations
- **Audience behavior patterns** (what they comment on, share, ignore)

This file is also loaded when Apex drafts LinkedIn posts, application answers, and cold outreach — so insights compound into Rui's actual writing.

---

## 9. MANUAL TRIGGERS

### Run analytics now (from terminal)
```bash
python3 ~/.openclaw/tools/linkedin-post-analytics.py week 10
python3 ~/.openclaw/tools/linkedin-post-analytics.py month 50
```

### Run cron job manually (from Discord/cmd)
```
@Bombot run cron apex-linkedin-analytics
```

### Post a new LinkedIn URL to #apex-career
Apex will automatically:
1. `web_fetch` the post URL
2. Analyze hook, topic, format, CTA, word count
3. Log to Notion with all metadata
4. Post brief analysis back to #apex-career

---

## 10. KNOWN LIMITATIONS & MITIGATIONS

| Limitation | Mitigation |
|---|---|
| LinkedIn impressions not available via Apify | Engagement Rate left blank unless manually entered. Focus on raw engagement (likes+comments+reposts) for ranking. |
| Apify may miss posts older than 30 days | Run with `posted_limit: "month"` to capture up to 30 days. For historical data, increase `max_posts`. |
| Performance tier is relative, not absolute | Thresholds (Viral >500, Strong >100, etc.) should be recalibrated quarterly as Rui's audience grows. |
| Topic/hook detection is keyword-based | Apex reviews and can override auto-classifications in the Insights field. |
| LinkedIn changes page structure | If Apify returns 0 posts, check actor version at apify.com or switch to backup actor. |

---

## 11. CREDENTIALS REFERENCE

| Credential | Location |
|---|---|
| `APIFY_TOKEN` | `~/.openclaw/workspace/.env` |
| `NOTION_API_KEY` | `~/.openclaw/workspace/.env` + `~/.zshrc` |
| Notion DB ID (Analytics) | `3154affb-d00c-814e-bc1a-d0d9072aad24` |
| Notion DB ID (Job Tracker) | `3124affb-d00c-81ad-95fe-fc5dc676c3eb` |
| LinkedIn Profile | `https://www.linkedin.com/in/rui-bom` |
| Discord Channel (apex-career) | `1476140537202475008` |
| Script path | `~/.openclaw/tools/linkedin-post-analytics.py` |

---

*Last updated: March 2026. Maintained by Apex.*
