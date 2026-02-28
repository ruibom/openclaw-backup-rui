# THREE-TIER MEMORY ARCHITECTURE
# Bombot HQ — All Agents
# Designed: 2026-02-27 by Brain
# Status: IMPLEMENTED

---

## Overview

The system implements three memory tiers across all 10 agents, plus a shared cross-agent layer.
Inspired by cognitive science: semantic (facts), episodic (events), procedural (skills).

```
~/.openclaw/workspace/
├── shared/
│   └── memory/
│       ├── semantic/
│       │   ├── RUI_PROFILE.md          ← Master facts about Rui (all agents read)
│       │   └── AGENT_REGISTRY.md       ← Agent roster, channels, capabilities
│       ├── episodic/
│       │   └── CROSS_AGENT_EVENTS.md   ← Significant events multiple agents need
│       └── procedural/
│           └── MEMORY_WRITE_PROTOCOL.md ← How ALL agents write/read memory
│
└── agents/
    └── {agent}/
        └── memory/
            ├── semantic/       ← Domain-specific stable facts
            ├── episodic/       ← Session logs, outcomes, events
            └── procedural/     ← Learned behaviors, patterns, playbooks
```

---

## Tier Definitions

### TIER 1 — SEMANTIC (Facts)
- **What lives here:** Stable facts, configurations, baselines, preferences
- **Change frequency:** Low — only when reality changes
- **Write rule:** Update immediately when a fact changes. Strike old value, add new.
- **Examples per agent:**
  - Shared: RUI_PROFILE.md (health baseline, career targets, identity)
  - Apex: CAREER_STATE.md (pipeline status, Apify config, Notion IDs)
  - Eros: DATING_STATE.md (active apps, funnel state, target profile)
  - Atlas: HEALTH_STATE.md (diffs from baseline, active priorities, supplement cycle)
  - Brain: DECISIONS_LOG.md (every major decision with date and reasoning)

### TIER 2 — EPISODIC (Events)
- **What lives here:** Timestamped records of what happened
- **Change frequency:** Every session — append-only, never edit
- **Write rule:** Always append at end of session. Even if "nothing happened."
- **Format:** `| Date | Task | Outcome | Flags |`
- **Examples per agent:**
  - All agents: SESSION_LOG.md in their episodic/ folder
  - Shared: CROSS_AGENT_EVENTS.md for system-wide events

### TIER 3 — PROCEDURAL (Skills)
- **What lives here:** Evidence-based learned behaviors, playbooks, what works/fails
- **Change frequency:** Medium — only when pattern confirmed over 2+ data points
- **Write rule:** Each entry must have: WHAT | EVIDENCE | CONFIDENCE | DATE
- **Confidence levels:** Low (<3 data points) | Medium (3–10) | High (10+ or strong signal)
- **Examples per agent:**
  - Bombot: cron delivery patterns, gateway recovery steps, routing rules
  - Apex: job verification checklist, LinkedIn comment formula
  - Eros: match patterns by geography, wave pattern behavior
  - Atlas: supplement timing, workout protocols, medical guardrails

---

## Cross-Agent Memory Sharing

### What is shared (all agents can read):
- `shared/memory/semantic/RUI_PROFILE.md` — master Rui profile
- `shared/memory/semantic/AGENT_REGISTRY.md` — agent roster and channels
- `shared/memory/episodic/CROSS_AGENT_EVENTS.md` — system-wide events
- `shared/memory/procedural/MEMORY_WRITE_PROTOCOL.md` — this protocol

### What stays private (agent-only):
- Everything in `{agent}/memory/` — specific to that domain

### Archiv is the memory custodian:
- Reads all agents' episodic logs weekly
- Promotes confirmed patterns to procedural tier
- Audits semantic facts monthly for staleness
- Writes cross-agent events to shared layer

---

## Agent Memory Ownership

| Agent | Semantic owns | Episodic owns | Procedural owns |
|-------|--------------|---------------|-----------------|
| Bombot | ROUTING_FACTS.md | SESSION_LOG.md | routing patterns, cron delivery rules |
| Apex | CAREER_STATE.md | SESSION_LOG.md | job scoring, LinkedIn voice patterns |
| Eros | DATING_STATE.md | SESSION_LOG.md | match patterns, opener tactics |
| Atlas | HEALTH_STATE.md | SESSION_LOG.md | supplement protocols, workout patterns |
| Pulse | PORTFOLIO_STATE.md | SESSION_LOG.md | CoinGecko patterns, reporting standards |
| Hana | LANGUAGE_STATE.md | SESSION_LOG.md | teaching patterns, vocabulary management |
| Archiv | KNOWLEDGE_BASE.md | SESSION_LOG.md | research patterns, content preferences |
| Illusion | MAGIC_STATE.md | SESSION_LOG.md | practice patterns, Eros integration |
| Hunter | RENTAL_STATE.md | SESSION_LOG.md | trust scoring, lead qualification |
| Brain | DECISIONS_LOG.md | SESSION_LOG.md | reasoning frameworks, decision patterns |

---

## Session Start Protocol (all agents, mandatory)

```
1. Load SOUL.md + AGENTS.md  (identity — always)
2. memory_search relevant query against own memory/ dir
3. For cross-domain queries: read shared/memory/semantic/RUI_PROFILE.md
4. Load domain-specific semantic file (e.g. CAREER_STATE.md for Apex)
5. Execute task
6. WRITE: append to episodic/SESSION_LOG.md
7. WRITE: update semantic if any fact changed
8. WRITE: update procedural if new pattern confirmed
9. WRITE: append to shared/episodic/CROSS_AGENT_EVENTS.md if cross-agent relevance
```

---

## Migration Map (existing files → new tiers)

| Agent | Old file | New tier | Action |
|-------|----------|----------|--------|
| Apex | RUI_LEARNING_LOG.md | Procedural | Content migrated to procedural/LEARNED_BEHAVIORS.md. Keep original as legacy reference. |
| Apex | ENGAGEMENT_LOG.md | Episodic | Future entries → episodic/SESSION_LOG.md. Old entries stay in place. |
| Apex | POST_STATS.md | Episodic | Future entries → episodic/SESSION_LOG.md. Old entries stay. |
| Eros | PATTERNS.md | Procedural | Content migrated. Keep original — Eros still references it in crons. |
| Eros | STATS.md | Episodic | Future entries → episodic/SESSION_LOG.md. |
| Atlas | WORKOUT_LOG.md | Episodic | Continue as-is. Mirror to episodic/SESSION_LOG.md for session-level entries. |
| Atlas | NUTRITION_LOG.md | Episodic | Same as above. |
| Atlas | SUPPLEMENT_LOG.md | Episodic | Same as above. |
| Atlas | BLOODWORK_LOG.md | Semantic | Bloodwork baselines = semantic facts. |
| Atlas | VITALITY_TRENDS.md | Procedural | Trend intelligence = procedural knowledge. |
| Archiv | memory/youtube_api_notes.md | Semantic | Migrated to memory/semantic/KNOWLEDGE_BASE.md |
| Apex | memory/Dimitris_prep.md | Episodic | Stays in memory/ — one-off event record. |

**Rule:** Old files are NOT deleted. The memory/ tier is additive. Old files remain valid references.
Agents update both old files (for backward compat with crons) AND new memory/ files going forward.

---

## Cron Integration (how memory write gets triggered automatically)

Add to each agent's heartbeat cron payload — end of message:

```
After completing all tasks:
1. Append session summary to ~/.openclaw/workspace/agents/{id}/memory/episodic/SESSION_LOG.md
2. Update ~/.openclaw/workspace/agents/{id}/memory/semantic/{STATE_FILE}.md if any facts changed
3. If cross-agent relevant: append to ~/.openclaw/workspace/shared/memory/episodic/CROSS_AGENT_EVENTS.md
```

---

## Archiv Weekly Consolidation Cron (to be created)

Schedule: Monday 09:00 JST
Task: Read all 10 agents' episodic/SESSION_LOG.md files from the past 7 days.
Identify patterns appearing 2+ times. Promote to relevant agent's procedural/LEARNED_BEHAVIORS.md.
Flag any semantic facts that appear stale. Post summary to #archiv-save.

---

## Design Principles

1. **Additive, never destructive** — old files stay. New tier is additive.
2. **Evidence-gated procedural** — patterns need 2+ confirmations before procedural
3. **Append-only episodic** — history is immutable. Use strikethrough for corrections.
4. **Archiv as custodian** — cross-agent consolidation lives in one place
5. **Cost-aware** — memory_search before loading whole files. Only load what's needed.
6. **Cron-compatible** — write instructions embedded in cron payloads, not just session prompts
