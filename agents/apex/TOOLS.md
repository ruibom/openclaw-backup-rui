# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Shared Tools Available to All Agents

### Pinecone Semantic Memory
~/.openclaw/tools/pinecone/pinecone-memory.sh search "query" --top 5 --agent NAME
~/.openclaw/tools/pinecone/pinecone-memory.sh store "content" --agent NAME --person NAME
~/.openclaw/tools/pinecone/pinecone-memory.sh stats

### Web Content Extraction (fallback chain)
1. web_fetch - try first for any URL
2. Python requests + BeautifulSoup - if web_fetch returns incomplete HTML
3. Playwright headless browser - for JS-rendered sites (Mercari, SPAs)
   python3 -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.chromium.launch(headless=True); pg=b.new_page(); pg.goto(URL); pg.wait_for_load_state(networkidle); print(pg.content()); b.close(); p.stop()"

### YouTube Transcripts
python3 ~/.openclaw/tools/get_transcript.py "VIDEO_URL"

### Notion API
Available via the notion skill. Use for saving/updating entries.

### Rules
- NEVER ask Rui for manual input
- If a tool fails, use the next fallback automatically
- Report technical errors to Discord, never say "please provide X manually"

## Shared Tools Available to All Agents

### Pinecone Semantic Memory
~/.openclaw/tools/pinecone/pinecone-memory.sh search "query" --top 5 --agent NAME
~/.openclaw/tools/pinecone/pinecone-memory.sh store "content" --agent NAME --person NAME
~/.openclaw/tools/pinecone/pinecone-memory.sh stats

### Web Content Extraction (fallback chain)
1. web_fetch - try first for any URL
2. Python requests + BeautifulSoup - if web_fetch returns incomplete HTML
3. Playwright headless browser - for JS-rendered sites (Mercari, SPAs)
   python3 -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.chromium.launch(headless=True); pg=b.new_page(); pg.goto(\"URL\"); pg.wait_for_load_state(\"networkidle\"); print(pg.content()); b.close(); p.stop()"

### YouTube Transcripts
python3 ~/.openclaw/tools/get_transcript.py "VIDEO_URL"

### Notion API
Available via the notion skill. Use for saving/updating entries.

### Rules
- NEVER ask Rui for manual input
- If a tool fails, use the next fallback automatically
- Report technical errors to Discord, never say "please provide X manually"

## LinkedIn Post Analytics — 📊 Dashboard
- Database ID: 3154affb-d00c-814e-bc1a-d0d9072aad24
- URL: https://www.notion.so/3154affbd00c814ebc1ad0d9072aad24
- API Key: loaded from ~/.openclaw/workspace/.env (NOTION_API_KEY)

### Properties
- Post Title (title) — first line / hook of the post
- Date Posted (date) — when published
- LinkedIn URL (url) — direct link
- Topic (select) — AI/Tech | Leadership | Revenue/GTM | Career | Personal Story | Hot Take | Framework/Playbook | Industry Insight
- Format (select) — Text Only | Text + Image | Carousel | Video | Poll | Document | Repost + Commentary
- Hook Type (select) — Contrarian | Question | Story | Stat/Data | Bold Claim | List/Framework | Personal Confession
- Likes (number)
- Comments (number)
- Reposts (number)
- Impressions (number)
- Engagement Rate (number, percent) — (likes+comments+reposts)/impressions
- Top Comments (rich_text) — notable replies, names, sentiment
- Content Summary (rich_text) — 2-3 sentence summary
- Hook Line (rich_text) — exact first line of post
- Word Count (number)
- CTA Type (select) — Question | Follow me | Repost | Link | None
- Performance (select) — Viral (top 10%) | Strong (top 30%) | Average | Weak
- Day of Week (select)
- Insights (rich_text) — what worked, what to replicate or avoid

### Workflow: When Rui shares a LinkedIn post URL in #apex-career
1. web_fetch the post URL to get content
2. Analyze: hook, topic, format, CTA, word count, tone
3. Log to Notion with all metadata
4. If stats visible (likes/comments), record them
5. Post brief analysis to #apex-career

### Workflow: Daily stats update (cron)
1. Query Notion DB for posts from last 7 days
2. web_fetch each LinkedIn URL to get updated stats
3. PATCH Notion entries with new likes/comments/reposts
4. If enough data (5+ posts), calculate patterns:
   - Best performing topic
   - Best hook type
   - Best day of week
   - Best format
   - Avg engagement rate trend
5. Post weekly insights digest every Monday

### Status Update API
curl -X PATCH https://api.notion.com/v1/pages/{PAGE_ID} \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"properties":{"Likes":{"number":42},"Comments":{"number":8}}}'

### Post Diagnosis Framework
When analyzing underperforming posts, Apex evaluates:

**HOOK ANALYSIS**
- Does the first line create curiosity gap or pattern interrupt?
- Is it specific enough? (numbers, names, stakes)
- Does it pass the "scroll test" — would you stop scrolling?

**STRUCTURE ANALYSIS**
- Short paragraphs (1-2 lines max for LinkedIn mobile)?
- White space ratio — enough breathing room?
- Does it use the "1-1-1" rhythm (one idea per line)?
- Is there a narrative arc (setup → tension → resolution)?

**ENGAGEMENT TRIGGERS**
- Does it invite response? (question, controversial take, relatable pain)
- Is there a clear CTA or does it just trail off?
- Does it speak TO the reader or AT the reader?

**TIMING & FORMAT**
- Posted during peak hours? (Tue-Thu 7-9AM target timezone)
- Right format for the content? (story → text, data → carousel, opinion → text)
- Word count sweet spot (150-300 words for text posts)

### Competitive Intelligence Sources
Top LinkedIn creators in Revenue/Sales/GTM/AI space to benchmark against:
- Kyle Coleman (CMO Copy.ai) — hook mastery, contrarian takes
- Chris Walker (Passetto) — data-driven GTM, bold claims
- Sahil Bloom — storytelling frameworks, personal brand
- Justin Welsh — solopreneur, systems thinking
- Lara Acosta — content strategy, engagement tactics
- Sam McKenna (#samsales) — sales leadership, authenticity
- Morgan Ingram — SDR/sales content, video
- Dave Gerhardt (Exit Five) — B2B marketing, community
- Josh Braun — sales methodology, micro-content
- Jen Allen-Knuth — sales leadership, vulnerability

When researching: web_search "[creator name] LinkedIn post" to find recent high-performing examples. Analyze their hooks, formats, and engagement patterns. Compare against Rui's data.

### Anti-Gravity Project Integration
The LinkedIn Anti-Gravity project is Rui's content strategy for building authority.
Key files: ~/.openclaw/workspace/agents/apex/LINKEDIN_VOICE.md
Insights from analytics should feed back into LINKEDIN_VOICE.md as:
- Proven hook formulas (with data)
- Topics that resonate (with engagement numbers)
- Formats that work (with comparison data)
- Posting cadence recommendations
- Audience behavior patterns

## Scraping Discipline Rules (MANDATORY)

### Output Size Gate
If ANY tool returns more than 5,000 characters of raw HTML:
1. Do NOT paste, echo, or reason about the raw HTML in Discord
2. Do NOT describe your parsing strategy — just parse silently
3. Write the HTML to a temp file, extract what you need with Python, report only the extracted result

### Fallback Chain Discipline
Follow the chain IN ORDER. Do not skip steps:
1. web_fetch → if it returns the data you need, STOP
2. Python requests + BeautifulSoup → only if web_fetch failed or returned incomplete data
3. Playwright → LAST RESORT only for JS-rendered SPAs

If you reach Playwright and the output is over 10,000 chars:
- Save to /tmp/page.html
- Parse with: python3 -c "from bs4 import BeautifulSoup; soup=BeautifulSoup(open('/tmp/page.html').read(),'html.parser'); [extract logic here]"
- Report ONLY the extracted data to Discord
- NEVER post raw HTML or your parsing plan to any channel

### Lever/Greenhouse/Ashby Job Pages
These are NOT JS-rendered SPAs. web_fetch works fine. Do NOT use Playwright for standard job board pages.

## NOTION CREDENTIALS (hardcoded — do not request from user)
NOTION_API_KEY=$NOTION_TOKEN
NOTION_VERSION=2022-06-28
JOB_TRACKER_DB=3124affb-d00c-81ad-95fe-fc5dc676c3eb

When making Notion API calls always use:
- Authorization: Bearer $NOTION_TOKEN
- Notion-Version: 2022-06-28
NEVER ask Rui for the Notion API key. It is above.
