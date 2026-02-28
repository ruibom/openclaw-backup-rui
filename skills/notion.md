# SKILL: Notion API

## Exact file path
This skill is at: ~/.openclaw/workspace/skills/notion.md
There is no subdirectory. Never look for notion/SKILL.md — it does not exist.

## API Details
- Endpoint: https://api.notion.com/v1/pages
- Method: POST to create, PATCH to update
- Authorization: Bearer $NOTION_TOKEN
- Notion-Version: 2022-06-28
- Database ID: 3134affb-d00c-81e7-8d5a-ecb12aac8f98

## Exact property names and types (use these exactly — no variations)
- Company (title) — company name
- Role (rich_text) — role title or "Intro Call" if no specific role
- Status (select) — RESEARCH | APPLIED | INTERVIEW SCHEDULED | INTERVIEW DONE | FOLLOW-UP SENT | OFFER | CLOSED
- Score (number) — fit score 1–10, leave blank for networking calls
- Source (select) — Inbound Referral | Newsletter | LinkedIn | Cold Outreach
- Comp (rich_text) — compensation range if known
- Stage (select) — Series A | Series B | Series C | Bootstrapped | Public
- Job Link (url) — original job posting URL or blank if inbound intro
- Contact Person (rich_text) — name, role, and LinkedIn URL of person who reached out
- Notes (rich_text) — research summary, 2–3 sentences max
- Interview Notes (rich_text) — post-interview debrief and sentiment read
- Interview Prep (url) — link to Interview Prep child page under Interview Prep folder
- Application Answers (url) — link to Application Answers child page under Application Answers folder
- Follow-up Sent (checkbox) — true once value-add follow-up is sent

## Folder IDs (for creating child pages)
- Interview Prep folder ID: 3134affb-d00c-81d5-822b-f942d126d2df
- Application Answers folder ID: 3134affb-d00c-819d-bd03-f13881f08393

## Workflow for saving a lead
1. Create Interview Prep page under Interview Prep folder (ID above). Title: "{Company} — Interview Prep". Record its URL.
2. Create Application Answers page under Application Answers folder (ID above) only when answers exist. Record its URL.
3. POST to /v1/pages with parent.database_id = 3134affb-d00c-81e7-8d5a-ecb12aac8f98 to create the tracker row.
4. Populate Interview Prep (url) and Application Answers (url) fields with the page URLs from steps 1–2.

## Output rule
After a successful Notion write, post ONLY this to Discord — nothing else:

✅ {Company} — {Role} logged
Score: {breakdown e.g. Remote:2 Comp:2 Senior:2 Stage:1 TZ:1 = 8/10}
Notion: {tracker row URL}
Interview Prep: {interview prep page URL}

Full brief is in Notion. Do not post the full prep package in Discord.

## Rules
- Use ONLY property names listed above — no others exist
- Always check response code — 200/201 = success, anything else = failure
- If error → report exact error immediately. Never say "Done" if it failed.
- Never assume a write succeeded without confirming the response.
- Never post the full prep package to Discord — only the 4-line summary above.
