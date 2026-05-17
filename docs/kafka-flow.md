# Kafka Event Flow

The trading API publishes every simulated order to the Kafka topic `orders`.

Flow:

Trading API → Kafka Topic: orders → Order Consumer

The consumer listens to the `orders` topic and prints every received order event.

Example event:

```json
{
  "symbol": "RELIANCE",
  "side": "SELL",
  "quantity": 173,
  "latency": 0.321,
  "status": "SUCCESS"
}