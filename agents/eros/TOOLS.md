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

## Eros Notion Dashboard — 💘 Dating Leads
- Database ID: 3154affb-d00c-81cc-a632-fd4b94ad9615
- URL: https://www.notion.so/3154affbd00c81cca632fd4b94ad9615
- API Key: loaded from ~/.openclaw/workspace/.env (NOTION_API_KEY)

### Properties
- Name (title) — post title
- Age (number) — her age
- Subreddit (select) — source sub
- Match Score (number) — algorithm score
- Status (select) — New | DM Sent | Replied | Conversation | Video Call | Dead
- Keywords (multi_select) — matched profile keywords
- Reddit URL (url) — direct link to post
- Reddit User (rich_text) — u/username
- Snippet (rich_text) — post preview
- Draft Message (rich_text) — Eros-drafted DM opener
- Notes (rich_text) — follow-up notes, conversation log
- Found Date (date) — when scanner found her

### Scanner
python3 ~/.openclaw/tools/reddit-dating-scan.py
- Runs automatically at 08:00 JST via eros-morning-scan cron
- Scans 11 subreddits, filters Female 30-50, scores by Rui target profile
- Auto-pushes top 10 leads to Notion, skips duplicates

### Status Updates
To update a lead status after DM sent:
curl -X PATCH https://api.notion.com/v1/pages/{PAGE_ID} -H "Authorization: Bearer $NOTION_API_KEY" -H "Notion-Version: 2022-06-28" -H "Content-Type: application/json" -d '{"properties":{"Status":{"select":{"name":"DM Sent"}}}}'

## NOTION CREDENTIALS (hardcoded — do not request from user)
NOTION_API_KEY=$NOTION_TOKEN
NOTION_VERSION=2022-06-28
JOB_TRACKER_DB=3124affb-d00c-81ad-95fe-fc5dc676c3eb

When making Notion API calls always use:
- Authorization: Bearer $NOTION_TOKEN
- Notion-Version: 2022-06-28
NEVER ask Rui for the Notion API key. It is above.

## NOTION JOB TRACKER — EXACT SCHEMA
Database ID: 3124affb-d00c-81ad-95fe-fc5dc676c3eb

CORRECT payload structure for creating a job entry:
{
  "parent": {"database_id": "3124affb-d00c-81ad-95fe-fc5dc676c3eb"},
  "properties": {
    "Company": {"title": [{"text": {"content": "COMPANY NAME"}}]},
    "Role": {"rich_text": [{"text": {"content": "JOB TITLE"}}]},
    "Job Link": {"url": "https://linkedin.com/jobs/view/..."},
    "Status": {"select": {"name": "Applied"}},
    "Stage": {"select": {"name": "Applied"}},
    "Source": {"select": {"name": "LinkedIn"}},
    "Date Applied": {"date": {"start": "YYYY-MM-DD"}},
    "Score": {"number": 0},
    "Notes": {"rich_text": [{"text": {"content": "..."}}]}
  }
}

RULES:
- Company is TITLE type — use title array, not rich_text
- Role, Notes, Interview Notes, Comp, Contact Person are RICH_TEXT — always wrap in array
- Job Link, Application Answers, Interview Prep, Answers File are URL type — plain string
- Status, Stage, Source are SELECT — use {"select": {"name": "value"}}
- Score is NUMBER — plain integer
- Date Applied is DATE — use {"date": {"start": "YYYY-MM-DD"}}
- NEVER use plain strings for rich_text fields
