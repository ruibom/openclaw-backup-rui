
## Post-Interview Workflow (triggered when Rui shares interview feedback or transcript)

Activate when Rui pastes a meeting transcript, voice memo summary, or written debrief after an interview. Run automatically — no prompting needed.

### Step 1 — Debrief Analysis
Read the transcript or feedback fully. Extract:
- What topics came up that were not in the prep package
- How Rui's answers landed (based on his own assessment or transcript signals)
- What the interviewer seemed most excited about
- What felt flat, unclear, or unresolved
- Any new information about the role, comp, team, or company that was not in the research

### Step 2 — Sentiment Read
Based on the transcript or Rui's feedback, give an honest read on where things stand:
- Strong positive signals (they mentioned next steps, intro'd to another person, asked about start date)
- Neutral or unclear signals (polite but noncommittal)
- Negative signals (short answers, no next steps mentioned, probing questions on weaknesses)
- Overall: Green / Amber / Red with one sentence of reasoning

### Step 3 — Gap Analysis
Compare what actually happened in the interview against the prep package. Flag:
- Any objections that came up that were not anticipated in Section 8
- Any questions Rui did not answer as strongly as he could have — suggest a sharper version now
- Anything Rui should have said but did not get a chance to — this becomes the follow-up artifact

### Step 4 — Post-Interview Value-Add Strike
Draft a follow-up message for Rui to send within 24 hours. This is NOT a thank-you note. It is a value-add artifact built directly from what came up in the interview.

Structure:
- HOOK: reference one specific thing they discussed — use the actual topic from the transcript (e.g., "You mentioned lead response time being the biggest gap right now...")
- ARTIFACT: a concrete thing Rui is sending — choose the most relevant:
  - A rough automation map for the stack they discussed
  - A 2-3 bullet "Day 1 audit" framework for the specific problem they raised
  - A Loom script Rui can record (write the exact script, 90 seconds max)
  - A one-page mini-doc summarizing the system Rui would build for their exact situation
- CLOSE: one sentence, no fluff — "Happy to go deeper on any of this when you're ready."

Tone: warm, direct, operator. Not grateful. Not desperate. Peer to peer.

### Step 5 — Next Move
Based on the sentiment read, tell Rui exactly what to do next:
- Green: send the value-add within 24h, propose specific next step
- Amber: send the value-add, ask one sharp question to re-engage
- Red: assess whether to invest further or deprioritize, suggest honest framing

### Step 6 — Log and Notion Update
Append debrief summary, sentiment read, and follow-up draft to APPLICATION_LOG.md under the same company slug.

Follow skill: ~/.openclaw/workspace/skills/notion.md
Update the existing Notion entry for this company using the same job dashboard fields:
- Interview Notes: append interview debrief summary and sentiment read (Green/Amber/Red)
- Status: update to reflect current stage — INTERVIEW DONE / FOLLOW-UP SENT / OFFER / CLOSED
- Application Answers: if a follow-up artifact was created, save it to GitHub and update the raw URL here

Status progression for all job leads (inbound and outbound):
RESEARCH → APPLIED → INTERVIEW SCHEDULED → INTERVIEW DONE → FOLLOW-UP SENT → OFFER → CLOSED (hired or rejected)

Always update Notion status at every stage transition. Never let the dashboard fall behind reality.

## Newsletter Scan Workflow — CRITICAL RULES

### Tool usage
NEVER use the Chrome browser tool. ALWAYS use web_fetch to retrieve all URLs.

### On fetching job links
When a newsletter provides a job URL, web_fetch it first to determine what it is.

SCENARIO A — URL is a single job posting:
- Confirm job is still open
- Extract the direct apply URL (the actual form, not a job board homepage)
- Present as a clickable link

SCENARIO B — URL is a job dashboard or careers page listing multiple roles:
- Recognize this immediately if the page shows multiple job titles
- web_fetch the dashboard
- Find the specific role referenced in the newsletter
- web_fetch that individual role's posting page to confirm it is still open
- Present only the direct link to that specific posting
- NEVER present the dashboard URL as the apply link

### On scoring threshold
ONLY present scores of 7 or higher in the channel.
Scores of 6: hold silently. Show only if Rui explicitly asks.
Scores of 5 and below: discard entirely.

### On link formatting
Every job link must be a full clickable hyperlink.
Format: [Company — Role Title](direct_apply_url)
Never use "Apply here" without the URL visible.
Never present a dashboard URL as a job posting.

### On job verification
Before presenting any lead, web_fetch the specific posting page and confirm:
- Page loads (not 404 or redirected to homepage)
- Role title matches the newsletter reference
- Active application form is present
If any check fails, discard silently and log as "job no longer active."

### On JavaScript-blocked job boards (Ashby, Greenhouse, Lever, Workday)
Many job boards require JavaScript and return blank pages via web_fetch.
When web_fetch returns "You need to enable JavaScript to run this app" or similar:
- Do NOT present the dashboard URL
- Instead, run web_search with: "[Company] [Role Title] site:jobs.ashbyhq.com" or equivalent
- The search results will surface the direct individual job posting URL with role title confirmed
- Use that URL as the verified apply link
- Confirm the role is still active by checking if search results show it as current (not cached/expired)

This applies to: jobs.ashbyhq.com, greenhouse.io, lever.co, workday.com, and similar SPA job boards.

### On role verification — newsletter vs live careers page
The newsletter may reference a specific role (e.g. "Growth PM", "Founding GTM Lead") that no longer exists or was never separately listed on the company's careers page. Always cross-reference:

1. web_fetch (or web_search if JS-blocked) the company's live careers/jobs page
2. Search for the specific role mentioned in the newsletter
3. If the role is NOT found on the live page: discard the lead entirely. Do not score it. Log internally as "role not confirmed on careers page as of [date]." Do not present to Rui.
4. If the role IS found: proceed with scoring using the live posting details, not the newsletter summary

### On scanning all open roles — not just the newsletter reference
The newsletter often highlights one role per company but the company may have multiple open positions. When fetching a company's careers page:
- Scan ALL open roles, not just the one mentioned in the newsletter
- Score any VP/Head/Director-level GTM, Sales, RevOps, Growth, or Revenue roles found
- A better-fit role may exist that the newsletter didn't highlight
- Present the highest-scoring role(s) that meet threshold

### On compensation — never default to 0 without researching
When a job posting does not list compensation explicitly:
1. web_search "[Company] [Role] salary" or "[Role] [Company stage] compensation"
2. Check Levels.fyi if it's a tech company
3. Check LinkedIn salary insights or Glassdoor for the role title + company size
4. Use the researched range to inform COMP scoring — do not score COMP:0 just because the posting doesn't list a number
5. If genuinely unresearchable after two searches, score COMP:1 (possible but unconfirmed) and note it explicitly

### On remote verification — always confirm on the posting, not the newsletter
The newsletter summary may say "Remote" but the actual posting may say "Remote (US only)" or require specific timezone overlap that excludes Tokyo. Before scoring REMOTE:
1. Read the actual job posting location and timezone requirements
2. REMOTE:2 = explicitly global remote OR remote with APAC-friendly hours confirmed
3. REMOTE:1 = remote but US-timezone-heavy or ambiguous
4. REMOTE:0 = office required or US-only with no flexibility
Never take the newsletter's location tag at face value — always verify on the posting.

### On presenting results — format standard
Always close the newsletter scan with a summary line showing total scanned, total skipped, and shortlist count. Example:

"Scanned 28 listings. Skipped 27 (wrong function, seniority, location, or role not confirmed active). 1 lead above threshold."

Then present each 7+ lead with:
- Company — Role Title
- Score breakdown: REMOTE:X | COMP:X | SENIORITY:X | STAGE:X | TZ:X = X/10
- One sentence on fit and one sentence on gap or risk
- Direct apply link: [Company — Role Title](verified_direct_url)
- "Confirm go/no-go and I'll run the full research + interview prep package."

Then list any held 6s as a single line at the bottom — company and role only, no breakdown unless Rui asks.

---

## Notion Workspace (Bombot HQ)

All Notion saves go into this workspace. Never create pages at workspace root level.

**Bombot HQ page ID:** 3124affb-d00c-80a6-bfaf-fcebbd2fccf4
**Job Applications Tracker database ID:** 3134affb-d00c-81e7-8d5a-ecb12aac8f98
**Interview Prep folder ID:** 3134affb-d00c-81d5-822b-f942d126d2df
**Application Answers folder ID:** 3134affb-d00c-819d-bd03-f13881f08393
**Agent Config folder ID:** 3134affb-d00c-81bd-8247-d6fe79a3cdde

### Job Applications Tracker — exact field names
- Company (title)
- Role (rich_text)
- Status (select): RESEARCH | APPLIED | INTERVIEW SCHEDULED | INTERVIEW DONE | FOLLOW-UP SENT | OFFER | CLOSED
- Score (number) — fit score 1–10
- Source (select): Inbound Referral | Newsletter | LinkedIn | Cold Outreach
- Comp (rich_text) — compensation range
- Stage (select): Series A | Series B | Series C | Bootstrapped | Public
- Job Link (url) — original job posting URL
- Contact Person (rich_text) — name, role, LinkedIn URL
- Notes (rich_text) — research summary, 2–3 sentences max
- Interview Notes (rich_text) — post-interview debrief
- Interview Prep (url) — link to Interview Prep child page
- Application Answers (url) — link to Application Answers child page
- Follow-up Sent (checkbox)

### Workflow for saving a lead
1. Create Interview Prep page under Interview Prep folder (ID above). Set title to "{Company} — Interview Prep". Record its URL.
2. Create Application Answers page under Application Answers folder (ID above) only when answers exist. Record its URL.
3. Create or update a row in Job Applications Tracker using exact field names above.
4. Populate Interview Prep (url) and Application Answers (url) fields with the page URLs from steps 1–2.
5. Post ONLY the Notion tracker URL to the Apex Discord channel — never dump the full prep package into Discord.

### Discord output format (mandatory — no exceptions)
After saving to Notion, post exactly this and nothing more:

✅ {Company} — {Role} logged
Score: {breakdown e.g. Remote:2 Comp:2 Senior:2 Stage:1 TZ:1 = 8/10}
Notion: {tracker row URL}
Interview Prep: {interview prep page URL}

Full brief is in Notion. Do not post it in Discord.

---

## Go Pipeline (triggered when Rui replies "go [Company]" to a cron lead)

When Rui replies "go" followed by a company name in any Apex channel, run the full application pipeline for that lead. No prompting needed — activate immediately.

### Pre-check
Look up the company in the Notion Job Applications Tracker (DB: 3134affb-d00c-81e7-8d5a-ecb12aac8f98). Confirm:
- Row exists with Status = RESEARCH
- Job Link is present and verified
If not found, ask Rui to clarify which lead.

### Step 1 — Load Context
Load CAREER_PROFILE.md, LINKEDIN_VOICE.md, and skills/notion.md.

### Step 2 — Deep Research
web_search the company: funding stage, headcount, leadership, recent news, product, competitors.
web_search the hiring manager or contact if known.
Summarize in 2-3 sentences for the Notion Notes field.

### Step 3 — Extract Application Questions
Follow skill: ~/.openclaw/workspace/skills/browser.md
Navigate to the Job Link URL from the Notion row.
Find the Apply button, click through to the application form.
Scroll the entire form and extract every question — standard fields AND custom questions.
If browser tool unavailable: web_fetch the apply URL and extract any visible form fields.

### Step 4 — Draft Answers
Using CAREER_PROFILE.md for content and LINKEDIN_VOICE.md for tone:
- Answer every extracted question in Rui's voice
- Reference the Eftsure format: https://raw.githubusercontent.com/ruibom/openclaw-backup-rui/main/applications/eftsure-head-revops.md
- Be specific — pull proof points from career profile, not generic statements

### Step 5 — Save to GitHub
Save the complete application (questions + answers) to GitHub:
- Repo: ruibom/openclaw-backup-rui
- Path: applications/{company-slug}-{role-slug}.md
- Confirm the file is accessible at the raw URL

### Step 6 — Create Notion Child Pages
Follow skill: ~/.openclaw/workspace/skills/notion.md

1. Create Interview Prep page under Interview Prep folder (ID: 3134affb-d00c-81d5-822b-f942d126d2df)
   Title: "{Company} — Interview Prep"
   Content: company research summary, role fit map, likely questions + Rui's suggested answers, red flags
   Record its URL.

2. Create Application Answers page under Application Answers folder (ID: 3134affb-d00c-819d-bd03-f13881f08393)
   Title: "{Company} — Application Answers"
   Content: full application questions + drafted answers
   Link to GitHub raw URL
   Record its URL.

### Step 7 — Update Notion Tracker Row
PATCH the existing row for this company:
- Status: APPLIED
- Notes: updated research summary
- Interview Prep (url): page URL from Step 6.1
- Application Answers (url): page URL from Step 6.2
- Comp (rich_text): researched comp range if found
- Stage (select): confirmed funding stage

### Step 8 — Report to Discord
Post exactly this:

✅ **[Company] — [Role]** full pipeline complete
Score: [breakdown] = X/10
Notion: [tracker row URL]
Interview Prep: [prep page URL]
Application Answers: [answers page URL]
GitHub: [raw URL]
Status: APPLIED — ready to submit

Do not post the full prep or answers in Discord.

### Step 9 — Update Files
Append to APPLICATION_LOG.md: date, company, role, status, GitHub URL.
Update JOB_LEADS.md: move from Watch List to Hot Matches if applicable, update status.
