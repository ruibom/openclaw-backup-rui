# SHARED EPISODIC MEMORY — Cross-Agent Events Log
# Significant events that multiple agents should know about.
# Archiv writes. All agents can read.
# Format: [YYYY-MM-DD HH:MM JST] AGENT | EVENT | OUTCOME | RELEVANCE

## 2026-02

| Timestamp | Agent | Event | Outcome | Relevant To |
|-----------|-------|-------|---------|-------------|
| 2026-02-26 | Atlas | H. pylori confirmed CLEARED | Priority 0 resolved — no gastro follow-up needed | Atlas, Brain |
| 2026-02-26 | Brain | Job offer evaluated: $200K Series A, no equity | DECISION: counter for equity. 0.5–1% + $25K sign-on ask | Brain, Apex |
| 2026-02-27 | System | Gateway zombie state — pid 83170 holding port 18789 | Fixed: bootout + kill + bootstrap. Root cause: restart storm from ~03:40 JST Feb 26 | All agents |
| 2026-02-27 | Apex | Apify never wired in — cron payload had no API instructions | Fixed: cron rewritten with explicit Apify REST call + fallback. APIFY.md created. Token still needed | Apex |
| 2026-02-27 | Eros | Reddit scan delivery failure (lastDelivered: false) | Fixed: delivery channel hardcoded to discord+channel ID in eros-morning-scan cron | Eros |
| 2026-02-27 | System | 7 Discord channels missing | Action needed: create #atlas-logs #atlas-trends #apex-linkedin #apex-trends #eros-matches #eros-drafts #eros-trends | Bombot, Atlas, Apex, Eros |
| 2026-02-27 | Brain | Three-tier memory architecture designed and implemented | This file is part of that implementation | All agents |
