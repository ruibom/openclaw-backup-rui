# APIFY.md — Apex External API Config

## Status
✅ ACTIVE — Token verified and working

## Apify API Key
APIFY_TOKEN=$APIFY_TOKEN

## Actor: LinkedIn Job Search Scraper (Search by Keywords)
Actor ID: harvestapi~linkedin-job-search
Endpoint: https://api.apify.com/v2/acts/harvestapi~linkedin-job-search/run-sync-get-dataset-items?token={APIFY_TOKEN}

## Input Parameters (JSON Body)
```json
{
  "jobTitles": ["VP Sales", "Head of Revenue", "VP RevOps", "Head of Sales", "Head of Growth"],
  "workplaceType": ["remote"],
  "postedLimit": "week",
  "maxItems": 20
}
```

## Parameter Notes
- `jobTitles`: Array of job titles to search (REQUIRED)
- `workplaceType`: Array with values "remote", "hybrid", or "office" (lowercase!)
- `postedLimit": One of "1h", "24h", "week", "month" (lowercase!)
- `maxItems`: Maximum jobs to return per search
- No cookies or LinkedIn account required
- Cost: ~$1 per 1k jobs scraped
- 98%+ success rate, fresh data (no caching)
