````md
# Trading Infrastructure Monitoring Platform

A production-style observability project that simulates trading infrastructure, order flow, FIX connectivity, Kafka event streaming, Prometheus metrics, and Grafana dashboards.

---

# Tech Stack

- Python
- FastAPI
- Docker
- Kafka
- Prometheus
- Grafana
- Kubernetes YAML
- OpenTelemetry Instrumentation

---

# Architecture

Trading API → Kafka Topic `orders` → Order Consumer  
Trading API → Prometheus → Grafana Dashboard

---

# Features

- Simulated trading order API
- Order success/failure simulation
- FIX session health simulation
- Market data health simulation
- Prometheus metrics endpoint
- Grafana monitoring dashboard
- Kafka producer and consumer
- Docker Compose setup
- Kubernetes deployment files

---

# Run Locally

```bash
docker compose up --build
````

Open:

```text
Trading API: http://127.0.0.1:8000
Prometheus: http://127.0.0.1:9090
Grafana: http://127.0.0.1:3000
```

---

# API Endpoints

```text
/health
/place-order
/metrics
/simulate-fix-disconnect
/simulate-fix-reconnect
/simulate-market-data-down
/simulate-market-data-up
```

---

# Kafka Flow

Every generated order is published to Kafka topic:

```text
orders
```

Consumer logs can be viewed using:

```bash
docker logs -f order-consumer
```

---

# Prometheus Metrics

```text
trading_orders_total
trading_failed_orders_total
trading_order_latency_seconds
fix_session_status
market_data_status
```

---

# Grafana Dashboard

Dashboard includes:

* Total trading orders
* Failed orders
* FIX session status
* Market data status
* P95 order latency

---

# Kubernetes

Kubernetes manifests are available in:

```text
k8s/
```

---

# Project Structure

```text
.
├── app
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── consumer
│   ├── Dockerfile
│   ├── consumer.py
│   └── requirements.txt
├── docker-compose.yml
├── docs
│   └── kafka-flow.md
├── grafana
├── k8s
│   ├── grafana-deployment.yml
│   ├── prometheus-deployment.yml
│   ├── trading-api-deployment.yml
│   └── trading-api-service.yml
├── kafka
├── prometheus
│   └── prometheus.yml
└── README.md
```

---

# Screenshots

## Grafana Dashboard

![Grafana Dashboard](screenshots/grafana-dashboard.png)

---

## Kafka Consumer Logs

![Kafka Consumer](screenshots/kafka-consumer.png)

---

## Prometheus Metrics

![Prometheus Metrics](screenshots/prometheus-metrics.png)

---

# Author

Shaive Sharma

```
```
