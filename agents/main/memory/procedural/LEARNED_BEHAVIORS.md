# BOMBOT PROCEDURAL MEMORY — Learned Behaviors
# Evidence-based routing and orchestration patterns.

## Routing Patterns

### Discord channel errors are structural, not transient
- WHAT: "Unknown target #channel" errors mean the channel doesn't exist — retrying won't fix it
- EVIDENCE: 2026-02-27 Atlas + Eros + Apex heartbeats all hit same error on secondary channels
- ACTION: On first channel error → log it, continue with available channels, flag to Rui at end of session
- CONFIDENCE: High

### Cron delivery `channel: last` fails for isolated agent sessions
- WHAT: Using `"channel": "last"` without explicit `"channel": "discord"` causes silent delivery failure for isolated agentTurn jobs
- EVIDENCE: eros-morning-scan ran ok (lastRunStatus: ok) but lastDelivered: false — fixed by adding channel: discord explicitly
- ACTION: All crons targeting Discord must use `{"mode": "announce", "channel": "discord", "to": "<channel_id>"}`
- CONFIDENCE: High

### Gateway restart storms: cause and pattern
- WHAT: Rapid-fire restart attempts + slow port release = zombie lock. Launchd keeps spawning, each spawn can't acquire lock, port stays held.
- EVIDENCE: 2026-02-27 — force-kills at 03:40, 03:46, 03:52, 03:57 JST before zombie settled
- ACTION: On "gateway already running" errors → bootout first, then kill PID, then bootstrap. Never just kill without bootout first.
- CONFIDENCE: High
