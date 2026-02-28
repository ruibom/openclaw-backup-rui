# linkedin-analytics

Extract LinkedIn post analytics (views, reactions, comments, reposts) without browser extension requirements.

## Installation

```bash
pip install -r tools/requirements.txt
playwright install chromium
```

## Usage

```python
from tools.linkedin_analytics import LinkedInAnalytics

# One-time: scrape a post (opens browser, saves cookies)
analytics = await LinkedInAnalytics().extract_post_analytics("https://linkedin.com/posts/...")

# Anytime: query stored analytics
data = LinkedInAnalytics().get_analytics()
```

## Data Storage

- Cookies: `~/.openclaw/workspace/agents/atlas/data/linkedin/cookies.json`
- Analytics: `~/.openclaw/workspace/agents/atlas/data/linkedin/post_analytics.json`

## Atlas Integration

This tool allows Atlas to pull LinkedIn engagement data on demand without manual browser extension clicks.
