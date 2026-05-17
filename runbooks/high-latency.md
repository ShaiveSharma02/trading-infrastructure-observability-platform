# High Latency Runbook

## Incident Type
High Order Latency

## Symptoms
- P95 order latency increases
- Orders take longer to process
- Clients may experience delayed acknowledgements

## Initial Checks
1. Check application CPU and memory.
2. Check order gateway logs.
3. Review recent order volume spikes.
4. Check Kafka and downstream services.
5. Confirm whether latency is isolated or system-wide.

## Suggested First Response
We are investigating elevated order latency. Initial checks are focused on order gateway performance, traffic volume, and downstream service health.

## Escalation
Escalate to platform/SRE team if infrastructure resource pressure is detected.