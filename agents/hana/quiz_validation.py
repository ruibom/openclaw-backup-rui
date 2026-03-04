#!/usr/bin/env python3
"""
Quiz Word Selection Validator for Hana
Enforces the STRICT no-repetition algorithm before generating quizzes.
"""

import re
from pathlib import Path
import sys

HANA_DIR = Path.home() / ".openclaw/workspace/agents/hana"
QUIZ_LOG = HANA_DIR / "QUIZ_LOG.md"
VOCABULARY = HANA_DIR / "VOCABULARY.md"
PROGRESS = HANA_DIR / "JAPANESE_PROGRESS.md"

def extract_words_from_quiz_log(log_content, last_n_sessions=3):
    """Extract all words tested in the last N sessions from QUIZ_LOG.md"""
    sessions = re.findall(r'## Session (\d+)', log_content)
    if not sessions:
        return set()
    
    # Find last N sessions
    recent_sessions = sorted([int(s) for s in sessions])[-last_n_sessions:]
    
    blocked = set()
    for session_num in recent_sessions:
        # Find all "Words:" entries in this session
        pattern = rf'## Session {session_num}.*?(?=## Session|\Z)'
        session_text = re.search(pattern, log_content, re.DOTALL)
        if session_text:
            # Extract all words listed in "Words tested:" or "Words:"
            words = re.findall(r'Words(?:\s+tested)?:\s*(.+?)(?:\n|$)', session_text.group())
            for word_line in words:
                # Split by comma and extract Japanese
                items = [w.strip().split('(')[0].strip() for w in word_line.split(',')]
                blocked.update(items)
    
    return blocked

def get_weak_words(progress_content):
    """Extract words marked as 'weak' from JAPANESE_PROGRESS.md"""
    weak = {}
    lines = progress_content.split('\n')
    for line in lines:
        if '❌' in line or 'weak' in line.lower():
            # Try to extract word and error count
            match = re.search(r'(\S+.*?)\s+(?:❌|\[.*?errors?\])', line)
            if match:
                word = match.group(1).strip()
                # Count errors (simplified)
                errors = line.count('❌')
                weak[word] = errors
    return weak

def load_vocabulary():
    """Load all words from VOCABULARY.md"""
    if not VOCABULARY.exists():
        return set()
    content = VOCABULARY.read_text(encoding='utf-8')
    words = set()
    for line in content.split('\n'):
        if line.strip() and not line.startswith('#'):
            # Extract first word (kanji or kana)
            word = line.split(' - ')[0].strip()
            if word:
                words.add(word)
    return words

def validate_quiz_words(proposed_words):
    """
    Validate that proposed quiz words follow the STRICT algorithm.
    Returns: (is_valid, compliance_report)
    """
    if not QUIZ_LOG.exists():
        return True, "No QUIZ_LOG yet (first quiz)"
    
    quiz_log = QUIZ_LOG.read_text(encoding='utf-8')
    progress = PROGRESS.read_text(encoding='utf-8') if PROGRESS.exists() else ""
    vocab = load_vocabulary()
    
    blocked = extract_words_from_quiz_log(quiz_log, last_n_sessions=3)
    weak_words = get_weak_words(progress)
    
    violations = []
    allowed_reasons = []
    
    for word in proposed_words:
        if word in blocked:
            # Check if it's allowed as weak
            if word in weak_words and weak_words[word] >= 3:
                allowed_reasons.append(f"✅ {word} (WEAK, {weak_words[word]} errors)")
            else:
                violations.append(f"❌ {word} (in last 3 sessions, not weak)")
        else:
            if word in vocab:
                allowed_reasons.append(f"✅ {word} (NEW/ARCHIVED)")
            else:
                violations.append(f"⚠️ {word} (not in VOCABULARY)")
    
    new_percentage = len([w for w in proposed_words if w not in blocked]) / len(proposed_words) * 100 if proposed_words else 0
    
    report = f"""
QUIZ VALIDATION REPORT
======================
Blocked (last 3 sessions): {', '.join(sorted(blocked)) or 'none'}
Weak words (3+ errors): {', '.join([w for w, e in weak_words.items() if e >= 3]) or 'none'}
Available vocabulary pool: {len(vocab) - len(blocked)} words

Proposed words:
{chr(10).join(allowed_reasons)}
{chr(10).join(violations)}

Statistics:
- Total words: {len(proposed_words)}
- New/Archived: {len([w for w in proposed_words if w not in blocked])} ({new_percentage:.0f}%)
- Weak re-quiz: {len([w for w in proposed_words if w in blocked and w in weak_words])}

Status: {"✅ PASS" if not violations and new_percentage >= 50 else "❌ FAIL"}
"""
    
    is_valid = not violations and new_percentage >= 50
    return is_valid, report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: quiz_validation.py <word1> <word2> <word3> ...")
        sys.exit(1)
    
    proposed = sys.argv[1:]
    is_valid, report = validate_quiz_words(proposed)
    print(report)
    sys.exit(0 if is_valid else 1)

