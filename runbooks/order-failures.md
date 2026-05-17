# Order Failures Runbook

## Incident Type
Order Failure Spike

## Symptoms
- Failed order count increases
- Clients may report rejected or failed orders
- Error rate may increase

## Initial Checks
1. Check failed order logs.
2. Review reject reasons.
3. Confirm if failures affect one symbol, client, or all orders.
4. Check downstream gateway health.
5. Validate recent configuration changes.

## Suggested First Response
We are investigating an increase in order failures. Initial checks are focused on reject reasons, affected scope, and downstream gateway health.

## Escalation
Escalate to application development team if failures are caused by application defects.