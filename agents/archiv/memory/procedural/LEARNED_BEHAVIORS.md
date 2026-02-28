# ARCHIV PROCEDURAL MEMORY — Learned Behaviors
# Evidence-based patterns only. Link to episodic source.
# Format: PATTERN | EVIDENCE | CONFIDENCE | DATE CONFIRMED

## Research Patterns

### YouTube transcripts require OAuth, not API key
- WHAT: YouTube Data API v3 captions.download requires OAuth 2.0 — API key alone returns 403
- EVIDENCE: youtube_api_notes.md (direct experience)
- CONFIDENCE: High (confirmed by API response)
- DATE: 2026-02-27
- ACTION: Use web_fetch on auto-generated transcript URLs or third-party extractors instead

### Memory consolidation: weekly cadence is optimal
- WHAT: Weekly review of agent episodic logs catches drift before it becomes noise
- EVIDENCE: Initial audit (2026-02-27) found existing "memory" files were ad-hoc and inconsistently structured — no episodic history preserved
- CONFIDENCE: Medium (first implementation, needs 4-week validation)
- DATE: 2026-02-27

## Content Patterns

### Rui prefers framework posts over narrative for reference material
- WHAT: When saving content for Rui, prioritize structured frameworks over long-form essays
- EVIDENCE: READING_LIST.md structure, LINKEDIN_VOICE.md framework sections
- CONFIDENCE: Medium
- DATE: 2026-02-27
