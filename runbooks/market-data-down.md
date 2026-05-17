# Market Data Down Runbook

## Incident Type
Market Data Feed Down

## Symptoms
- Market data status is 0
- Prices may appear stale or unavailable
- Trading decisions may be impacted

## Initial Checks
1. Check market data feed process.
2. Verify feed handler logs.
3. Confirm upstream provider connectivity.
4. Check if issue affects one symbol, one market, or all feeds.

## Suggested First Response
We are investigating a possible market data feed issue. Initial checks are focused on feed handler status, provider connectivity, and scope of impact.

## Escalation
Escalate to market data/vendor support if upstream feed is unavailable.