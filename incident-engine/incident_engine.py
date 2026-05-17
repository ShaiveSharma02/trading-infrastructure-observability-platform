from kafka import KafkaConsumer
from sklearn.ensemble import IsolationForest
import numpy as np
import json
import time

print("Starting Incident Intelligence Engine...", flush=True)

KAFKA_TOPIC = "orders"
KAFKA_BOOTSTRAP = "kafka:9092"

latency_history = []

def recommend_runbook(incident_type):
    runbooks = {
        "FAILED_ORDER": "runbooks/order-failures.md",
        "HIGH_LATENCY": "runbooks/high-latency.md",
        "FIX_DISCONNECT": "runbooks/fix-disconnect.md",
        "MARKET_DATA_DOWN": "runbooks/market-data-down.md"
    }

    return runbooks.get(incident_type, "No runbook found")


def generate_incident_summary(incident_type, order):
    if incident_type == "FAILED_ORDER":
        return {
            "incident_type": "Order Failure",
            "severity": "Medium",
            "summary": f"Order failure detected for {order.get('symbol')} {order.get('side')} order.",
            "recommended_runbook": recommend_runbook("FAILED_ORDER")
        }

    if incident_type == "HIGH_LATENCY":
        return {
            "incident_type": "High Latency",
            "severity": "High",
            "summary": f"High latency detected. Current latency: {round(order.get('latency'), 3)} seconds.",
            "recommended_runbook": recommend_runbook("HIGH_LATENCY")
        }

    return {
        "incident_type": "Unknown",
        "severity": "Low",
        "summary": "Unknown incident detected.",
        "recommended_runbook": "No runbook found"
    }


def is_latency_anomaly(latency):
    latency_history.append(latency)

    if len(latency_history) < 10:
        return False

    recent_data = np.array(latency_history[-50:]).reshape(-1, 1)

    model = IsolationForest(
        contamination=0.15,
        random_state=42
    )

    model.fit(recent_data)

    prediction = model.predict([[latency]])

    return prediction[0] == -1


consumer = None

while consumer is None:
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP,
            auto_offset_reset="latest",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

        print("Incident Engine connected to Kafka!", flush=True)

    except Exception as e:
        print("Kafka not ready for Incident Engine...", flush=True)
        print(e, flush=True)
        time.sleep(5)


for message in consumer:
    order = message.value

    print("\nOrder received by Incident Engine:", flush=True)
    print(order, flush=True)

    if order.get("status") == "FAILED":
        incident = generate_incident_summary("FAILED_ORDER", order)
        print("\nINCIDENT DETECTED:", flush=True)
        print(incident, flush=True)

    latency = order.get("latency", 0)

    if is_latency_anomaly(latency):
        incident = generate_incident_summary("HIGH_LATENCY", order)
        print("\nML ANOMALY DETECTED:", flush=True)
        print(incident, flush=True)