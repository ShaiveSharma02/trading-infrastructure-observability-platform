from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, Gauge
from kafka import KafkaProducer
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

import random
import time
import json
import os

app = FastAPI(
    title="Trading Infrastructure Monitoring Platform"
)

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------

orders_total = Counter(
    "trading_orders_total",
    "Total number of trading orders"
)

failed_orders_total = Counter(
    "trading_failed_orders_total",
    "Total failed trading orders"
)

order_latency = Histogram(
    "trading_order_latency_seconds",
    "Trading order latency"
)

fix_session_status = Gauge(
    "fix_session_status",
    "FIX session status"
)

market_data_status = Gauge(
    "market_data_status",
    "Market data feed status"
)

# Initial healthy state
fix_session_status.set(1)
market_data_status.set(1)

# -----------------------------
# KAFKA CONFIG
# -----------------------------

KAFKA_BOOTSTRAP = os.getenv(
    "KAFKA_BOOTSTRAP",
    "kafka:9092"
)

def get_kafka_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        return producer
    except Exception:
        return None

producer = get_kafka_producer()

# -----------------------------
# API ENDPOINTS
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Trading Infrastructure Monitoring Platform Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/place-order")
def place_order():

    orders_total.inc()

    simulated_latency = random.uniform(0.01, 0.8)

    with order_latency.time():
        time.sleep(simulated_latency)

    order = {
        "symbol": random.choice(
            ["AAPL", "MSFT", "TSLA", "INFY", "RELIANCE"]
        ),
        "side": random.choice(
            ["BUY", "SELL"]
        ),
        "quantity": random.randint(1, 1000),
        "latency": simulated_latency
    }

    # Simulate failures
    if random.random() < 0.15:

        failed_orders_total.inc()

        order["status"] = "FAILED"
        order["reason"] = "Simulated order gateway failure"

    else:
        order["status"] = "SUCCESS"

    # Send event to Kafka
    if producer:
        producer.send("orders", order)

    return order

# -----------------------------
# FIX SESSION SIMULATION
# -----------------------------

@app.get("/simulate-fix-disconnect")
def simulate_fix_disconnect():

    fix_session_status.set(0)

    return {
        "status": "FIX session disconnected"
    }

@app.get("/simulate-fix-reconnect")
def simulate_fix_reconnect():

    fix_session_status.set(1)

    return {
        "status": "FIX session reconnected"
    }

# -----------------------------
# MARKET DATA SIMULATION
# -----------------------------

@app.get("/simulate-market-data-down")
def simulate_market_data_down():

    market_data_status.set(0)

    return {
        "status": "Market data feed down"
    }

@app.get("/simulate-market-data-up")
def simulate_market_data_up():

    market_data_status.set(1)

    return {
        "status": "Market data feed healthy"
    }

# -----------------------------
# PROMETHEUS + OTEL
# -----------------------------

Instrumentator().instrument(app).expose(app)

FastAPIInstrumentor.instrument_app(app)