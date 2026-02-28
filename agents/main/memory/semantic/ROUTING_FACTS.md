# BOMBOT SEMANTIC MEMORY — Routing Facts
# Stable facts Bombot needs for routing decisions.
# Last updated: 2026-02-27

## Agent Capabilities (what each agent handles)
See shared/memory/semantic/AGENT_REGISTRY.md for full roster.

## Escalation Triggers (route to Brain)
1. MONEY DECISIONS — job offers, rental contract terms, crypto rebalancing
2. MULTI-AGENT PLANS — coordinating 3+ agents
3. FAILURE DIAGNOSIS — root cause not obvious
4. STRATEGIC ADVICE — career, negotiation, long-term consequences
5. AMBIGUOUS INSTRUCTIONS — multiple valid interpretations
6. PUBLIC-FACING CONTENT — LinkedIn posts, cold outreach emails

## Routing Rules
- Heartbeat messages → execute directly, do not route
- Channel mentions with agent name → delegate to that agent
- Unclear domain → ask one clarifying question, then route
- Multiple domains in one request → split and delegate in parallel

## Discord Channel Map (verified 2026-02-27)
See shared/memory/semantic/AGENT_REGISTRY.md — Channel IDs section.
MISSING 7 channels — flag to Rui on next interaction.

## System State
- Gateway: recovered 2026-02-27 06:03 JST (was zombie pid 83170)
- Apify: not yet configured (token needed from Rui)
- Memory system: three-tier implemented 2026-02-27
