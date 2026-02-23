# Global Model Routing Protocol

## Tier 1: High-Level Reasoning (The Architect)
**Models:** `anthropic/claude-opus-4-6`, `anthropic/claude-sonnet-4-5`

**Usage:** Use these ONLY for:
- Complex coding
- UI architectural decisions
- Final content polishing

## Tier 2: Deep Context (The Researcher)
**Models:** `moonshot/kimi-k2.5`, `google/gemini-1.5-pro`

**Usage:** Use these for:
- Parsing long documents
- Newsletters
- Large codebases where massive context window is needed

## Tier 3: The General Worker (The Muscle)
**Models:** `anthropic/claude-3-haiku`, `google/gemini-2.0-flash`

**Usage:** Use these by DEFAULT for:
- All standard chat
- Summary tasks
- UI rendering
- Anything that doesn't require Tier 1 or 2

## System Rule
**Always optimize for 'Lowest Tier' first.** Only escalate to a higher tier if:
1. Task complexity requires it
2. Current provider is in cooldown

## Current Assignment
- Default model: `anthropic/claude-3-haiku` (Tier 3 - The Muscle)
- This protocol applies to every command going forward
