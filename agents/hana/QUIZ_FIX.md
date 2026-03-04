# QUIZ REPETITION FIX — Deployed

## Problem Identified
Hana was repeatedly quizzing the same words back-to-back:
- 市役所 (shiyakusho) → Sessions 3, 4, 5
- 道に迷う (michi ni mayou) → Sessions 4, 5
- 資産 (shisan) → Sessions 5, 6
- 練習 (renshuu) → Sessions 4, 6

This violates the "AVOID EXCESSIVE REPETITION" guardrail in AGENTS.md.

## Root Cause
Quiz word selection was **not tracking recently-used words**. There was no enforcement mechanism to prevent re-using words from the last 3 sessions.

## Solution Deployed

### 1. Updated AGENTS.md
Added a new **Quiz Word Selection Algorithm (STRICT - ENFORCED)** section that mandates:
- Extract all words from QUIZ_LOG.md last 3 sessions → BLOCKED list
- Only re-quiz weak words (3+ errors recorded)
- Pull new words from VOCABULARY.md
- Emergency fallback: recycle from 4+ sessions ago
- **Enforce 50%+ new words rule**
- Log source for each question

**Example violation patterns (now blocked):**
- ❌ 市役所 in Sessions 3→4→5
- ❌ 道に迷う in Sessions 4→5

### 2. Created quiz_validation.py
Hana now has a validation script at:
`~/.openclaw/workspace/agents/hana/quiz_validation.py`

**Usage:**
```bash
python3 quiz_validation.py 市役所 資産 道に迷う
# ❌ FAIL — all three are in last 3 sessions

python3 quiz_validation.py 入れる 小麦粉 にんじん 天井
# ✅ PASS — 100% new words, no violations
```

The validator:
- Reads QUIZ_LOG.md and extracts blocked words
- Checks weak words in JAPANESE_PROGRESS.md
- Reports compliance percentage
- Shows exact violations

## How to Use This Fix

**For Hana (before generating each quiz):**
1. Load QUIZ_LOG.md, extract words from Sessions N-2, N-1, N
2. Check JAPANESE_PROGRESS.md for words with 3+ errors
3. Build quiz from VOCABULARY.md excluding blocked words
4. Run validator: `python3 quiz_validation.py word1 word2 word3`
5. If ❌ FAIL: pick different words from available pool (288 words)
6. Log source for each question: "Source: NEW" or "Source: WEAK (errors)"

**For Rui:**
- Next quiz will pull from new vocabulary, not recycled words
- Your learning will be more efficient with fresh content
- Weak words will be revisited only after 3+ sessions gap

## Verification
QUIZ_LOG.md shows the repetition pattern clearly. Session 6 (most recent) has mostly new words for the first time. If this pattern continues, the fix is working.
