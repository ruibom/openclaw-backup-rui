# Cost Tracking System

Track daily OpenClaw API costs to optimize spending.

## Strategy

**Default:** Kimi 2.5 (~$0.30-1.20/1M tokens)  
**Brain Heavy:** Claude Sonnet 4.5 (~$3-15/1M tokens)  
**Extreme:** Claude Opus 4.6 (~$15-75/1M tokens)

## Quick Commands

```bash
# Check today's usage
./cost-tracker.sh today

# Check last 7 days
./cost-tracker.sh week

# Manual log (if needed)
./cost-tracker.sh log kimi 10000 500
```

## Files

- `model-pricing.json` - Pricing reference
- `cost-tracker.sh` - Cost calculator
- `logs/YYYY-MM-DD.json` - Daily usage logs

## Auto-Logging (TODO)

Set up a heartbeat task or cron to automatically log session usage periodically.
