# APEX PROCEDURAL MEMORY — Learned Behaviors
# Migrated from RUI_LEARNING_LOG.md + new patterns from 2026-02-27 session.

## Job Verification Patterns

### Always verify job link leads to active application form (not careers homepage)
- WHAT: Many job links go to generic careers pages. Must web_fetch and confirm active application form present.
- EVIDENCE: Mews job removed in September — added without verification. CrowdStrike link went to generic page.
- ACTION: web_fetch every URL before scoring. Check for "removed/expired/404" AND that Apply button exists.
- CONFIDENCE: High (confirmed by user feedback)

### Score before Notion — never add below 8
- WHAT: Adding 2/5 or 3/5 fits to Notion wastes Rui's time and clutters the tracker
- EVIDENCE: Direct feedback from Rui session
- ACTION: Score first. Only run full pipeline (research + Notion + GitHub) for 8+. Flag 7 to Rui. Discard below.
- CONFIDENCE: High

### Comp scoring: research don't default to 0
- WHAT: Many postings don't list comp. Don't score COMP:0 just because it's not listed.
- ACTION: web_search "[Company] [Role] salary" + Levels.fyi + Glassdoor. Score COMP:1 if unresearchable.
- CONFIDENCE: High

### Remote verification: always check posting, not newsletter
- WHAT: Newsletter says "Remote" but posting may say "Remote US only" which is REMOTE:0 for Rui
- ACTION: Always read actual posting location/timezone requirements before scoring REMOTE.
- CONFIDENCE: High

## LinkedIn Engagement Patterns

### Comment structure that drives profile visits
- WHAT: Insightful observation → proof point from Penbrothers → universal truth
- EVIDENCE: LINKEDIN_VOICE.md — practitioner authority pattern
- ACTION: Never open with "Great post!" Never close with "Thoughts?" Lead with the insight.
- CONFIDENCE: Medium (not yet validated with data)

### Voice DNA: operator-first, fragment-heavy
- WHAT: Rui's voice uses short fragments, present-tense stories, contrast pairs, no corporate jargon
- EVIDENCE: LINKEDIN_VOICE.md vocabulary guardrails
- KEY TERMS: "A-players", "Operational Alpha", "Revenue Architecture", "Complexity Trap"
- AVOID: "thrilled", "passionate", "game-changing", "What do you think?"
- CONFIDENCE: High
