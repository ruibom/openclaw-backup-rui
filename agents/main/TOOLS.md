# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Dating Match Escalation Strategy

Most matches are **geographically dispersed** (not local). The escalation funnel is:

1. **Flirt/Banter Phase** — Build rapport, establish chemistry via text
2. **Image Sharing Phase** ← **CURRENT FOCUS** — Get her to send personal photos (selfies, lifestyle shots)
3. **Video Call Phase** — Once images confirm attraction, move to video
4. **Meeting/Logistics** — Real-world plans (if both invested)

**Key:** Do not skip to video calls until she's already invested via image sharing. Images = commitment signal that she's serious about you.

### Escalation Tactics for Image Sharing
- Compliment her current profile photos → ask for something more casual/personal
- "Send me a real smile pic" or "What do you look like without the glam?"
- Playful challenge: "Prove you're real — send me something candid"
- Share a selfie first to prompt reciprocation
- Build enough rapport so she *wants* to share more

### Tools & Workflow
- **eros agent:** Handles conversation analysis, tone, next-move strategy
- **#eros-matches:** CRM channel for profile tracking and conversation escalation notes
- When routing to eros: Always include full conversation context (screenshots of message threads, not just profile photos)

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
