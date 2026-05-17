from kafka import KafkaConsumer
import json
import time

print("Starting Kafka consumer...", flush=True)

consumer = None

while consumer is None:
    try:
        consumer = KafkaConsumer(
            "orders",
            bootstrap_servers="kafka:9092",
            auto_offset_reset="earliest",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

        print("Connected to Kafka!", flush=True)

    except Exception as e:
        print("Kafka not ready yet...", flush=True)
        print(e, flush=True)
        time.sleep(5)

for message in consumer:
    order = message.value

    print("\nNew Order Event Received:", flush=True)
    print(order, flush=True)

    if order["status"] == "FAILED":
        print("ALERT: Failed order detected!", flush=True)