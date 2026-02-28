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
