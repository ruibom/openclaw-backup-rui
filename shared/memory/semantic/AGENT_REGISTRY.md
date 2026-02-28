# SHARED SEMANTIC MEMORY — Agent Registry
# Maps agent IDs to roles, channels, and capabilities.
# Last updated: 2026-02-27

## Agent Roster

| ID | Name | Domain | Discord Channel | Model | Primary Files |
|----|------|--------|-----------------|-------|---------------|
| main | Bombot | Orchestration / Routing | #general, #bombot-log | kimi-k2.5 | SOUL.md, AGENTS.md |
| apex | Apex | Career / LinkedIn / Jobs | #apex-leads, #apex-linkedin, #apex-trends | gemini-2.5-flash | CAREER_PROFILE.md, LINKEDIN_VOICE.md |
| eros | Eros | Dating / Romance | #eros-romance, #eros-matches, #eros-drafts, #eros-trends | gemini-2.5-flash | MATCHES.md, PLAYBOOK.md |
| atlas | Atlas | Health / Fitness / Nutrition | #atlas-vitality, #atlas-logs, #atlas-trends | claude-haiku-4-5 | HEALTH_PROFILE.md, SUPPLEMENTS.md |
| pulse | Pulse | Crypto / Finance | #pulse-crypto | gemini-2.5-flash | PORTFOLIO.md, CRYPTO_ALERTS.md |
| hana | Hana | Japanese Language | #hana-lessons | claude-haiku-4-5 | VOCABULARY.md, JAPANESE_PROGRESS.md |
| archiv | Archiv | Knowledge / Research / Memory | #archiv-save | gemini-2.5-flash | READING_LIST.md |
| illusion | Illusion | Magic / Cardistry | #illusion-practice | kimi-k2.5 | MAGIC_REPERTOIRE.md |
| hunter | Hunter | Rental / Harajuku Apartment | #hunter-leads, #hunter-log | kimi-k2.5 | RENTAL_LEADS.md |
| brain | Brain | Deep Reasoning / Escalation | #brain-cmd | claude-sonnet-4-6 | SOUL.md, AGENTS.md |

## Escalation Path
Bombot → Brain (for 6 categories: MONEY, MULTI-AGENT, FAILURE, STRATEGY, AMBIGUOUS, PUBLIC-FACING)

## Channel IDs (verified 2026-02-27)
- #eros-romance: 1476129505071595631
- #atlas-vitality: 1476134301778055178
- #apex-leads: 1476140537202475008 (note: 1476141186271019048 also seen)
- #hunter-leads: 1476415682873917462
- #illusion-practice: 1476415159361605845
- #hana-lessons: 1476411539178127533
- #pulse-crypto: 1476410224171552939
- #bombot-log: (from cron config)
- MISSING: #atlas-logs, #atlas-trends, #apex-linkedin, #apex-trends, #eros-matches, #eros-drafts, #eros-trends
