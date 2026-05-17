# FIX Disconnect Runbook

## Incident Type
FIX Session Disconnect

## Symptoms
- FIX session status is 0
- Orders may not flow to the exchange or broker
- Clients may report order routing issues

## Initial Checks
1. Check FIX session heartbeat.
2. Verify network connectivity to counterparty.
3. Check gateway logs for logout or reject messages.
4. Confirm whether issue is client-side, network-side, or exchange/broker-side.

## Suggested First Response
We are investigating a potential FIX connectivity issue. Initial checks are focused on session heartbeat, gateway logs, and network connectivity. We will provide an update once the session state is confirmed.

## Escalation
Escalate to network/infrastructure team if connectivity failures are detected.