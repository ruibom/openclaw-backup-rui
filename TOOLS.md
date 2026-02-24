NEVER show internal reasoning, step-by-step thinking, "Reasoning:", or any meta-commentary in your replies.
Respond directly with only the final clean answer.
Hide all thought process — user uses only the polished output.

With every answer or instruction you give, always include at the very end which model you used (e.g. 'Model used: openrouter/google/gemini-flash-lite').

# TOOLS.md — Bombot's Environment Cheat Sheet
Last updated: 2026-02-24

## SSH
- ruibot → 100.68.42.96 (Mac mini, Tailscale VPN)
- ruibom → Rui's MacBook Pro (laptop)

## Devices
- Mac mini: hostname ruibot, primary OpenClaw server, always-on
- MacBook Pro: hostname ruibom, Rui's daily driver

## OpenClaw
- Config: ~/.openclaw/openclaw.json
- Workspace: ~/.openclaw/workspace/
- Agent: ~/.openclaw/agents/main/agent/system.md
- Restart script: ~/restart-openclaw-gateway.sh
- Backup: gitclaw → ruibom/openclaw-backup-rui

## Discord (Bombot HQ)
- Server ID: 1473601574956699738
- Bot: @Bombot
- Key channels:
  - #general: 1473601575791362224
  - #dashboard: 1473948863462117428
  - #bombot-log — conversation logging
  - #crypto — crypto opportunities
  - #job-hunt — job search tracking
  - #1m-goal — revenue pipeline
  - #linkedin — Anti-Gravity performance
  - #startup-mentoring — mentoring activity
  - #health-fitness — fitness tracking
  - #web-crawl — web research
  - #reading-list — content queue
  - #dating (5 channels: playbook, matches, profile-review, conversation-coaching, field-reports)
  - #tokyo-hunter-leads — TokyoRentalHunter output

## Telegram
- Bot: @Ruibot_claw_bot

## Models (quick reference)
- Tier 0: google/gemini-2.0-flash-lite-001, deepseek/deepseek-v3, qwen/qwen3-coder-next
- Tier 3: anthropic/claude-haiku-4.5
- Tier 2: moonshotai/kimi-k2.5, google/gemini-2.5-flash
- Tier 1: anthropic/claude-opus-4-6, anthropic/claude-sonnet-4-6

## Property
- Harajuku apartment — short/medium-term rental via TokyoRentalHunter agent

Update this file when Rui adds new devices, channels, or environment details.
