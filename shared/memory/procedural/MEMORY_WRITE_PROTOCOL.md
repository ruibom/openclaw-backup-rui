# SHARED PROCEDURAL MEMORY — Memory Write Protocol
# How ALL agents write and retrieve memory. Mandatory reading.
# Last updated: 2026-02-27

## The Three Tiers

### TIER 1 — SEMANTIC (Facts)
**What:** Stable facts, preferences, baselines, configurations.
**Changes:** Rarely — only when something fundamentally changes.
**Where:**
- `shared/memory/semantic/` — facts true across all agents
- `{agent}/memory/semantic/` — facts specific to this agent's domain
**Format:** Markdown with clear headers. Timestamped updates at top.
**Who writes:** The agent that owns the domain. Archiv for cross-domain facts.
**Examples:** health baseline, career profile, crypto holdings, agent registry

### TIER 2 — EPISODIC (Events)
**What:** Timestamped interactions, session outcomes, decisions made, things that happened.
**Changes:** Append-only. Never edit past entries.
**Where:**
- `shared/memory/episodic/` — events relevant to multiple agents
- `{agent}/memory/episodic/` — events relevant to this agent only
**Format:** Table rows: `[YYYY-MM-DD HH:MM JST] | Event | Outcome | Tags`
**Who writes:** Any agent, after any significant session or outcome.
**Examples:** job application submitted, match escalated, supplement cycle started, price alert triggered

### TIER 3 — PROCEDURAL (Skills)
**What:** Learned behaviors, playbooks, what works, what failed, optimized workflows.
**Changes:** Updated when patterns are confirmed with evidence (not hunches).
**Where:**
- `shared/memory/procedural/` — universal agent behaviors
- `{agent}/memory/procedural/` — domain-specific learned behaviors
**Format:** Sections: WHAT WORKS | WHAT FAILS | CURRENT BEST PRACTICE | EVIDENCE
**Who writes:** Any agent when a pattern is confirmed over 2+ data points.
**Examples:** LinkedIn comment style that drives profile visits, supplement timing that improves sleep, message openers that get replies

---

## Write Rules (mandatory for all agents)

1. **After every session** — write to episodic. Even if just: "scan ran, 0 leads found."
2. **When a fact changes** — update semantic immediately. Old values get struck out, not deleted.
3. **When a pattern is confirmed** — append to procedural with evidence.
4. **Never delete** — use ~~strikethrough~~ for superseded info. Preserve history.
5. **Always timestamp** — YYYY-MM-DD HH:MM JST on every entry.
6. **Keep semantic lean** — facts only. No narrative. No opinions.
7. **Keep episodic append-only** — never edit existing rows.
8. **Keep procedural evidence-based** — link to episodic entry that confirmed the pattern.

---

## Retrieval Rules (how agents use memory)

### On session start (mandatory recall):
```
1. Load own SOUL.md + AGENTS.md (identity)
2. memory_search relevant query against own memory/ dir
3. For cross-domain queries: read shared/memory/semantic/RUI_PROFILE.md
```

### On task completion (mandatory write):
```
1. Episodic: append outcome to {agent}/memory/episodic/SESSION_LOG.md
2. Semantic: update any facts that changed
3. Procedural: if new pattern confirmed, append to {agent}/memory/procedural/LEARNED_BEHAVIORS.md
4. If cross-agent relevance: append to shared/memory/episodic/CROSS_AGENT_EVENTS.md
```

### Archiv's special role:
- Archiv is the memory custodian. It consolidates, deduplicates, and promotes patterns.
- Weekly: Archiv reviews all agents' episodic logs and promotes confirmed patterns to procedural.
- Monthly: Archiv reviews semantic facts for staleness and flags updates needed.
