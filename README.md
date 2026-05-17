````md
# Trading Infrastructure Observability & Incident Intelligence Platform

A production-style trading infrastructure monitoring and incident intelligence platform built using FastAPI, Kafka, Prometheus, Grafana, Docker, Kubernetes, and AI/ML-based anomaly detection.

---

# Architecture

Trading API → Kafka Topic `orders` → Order Consumer

Trading API → Kafka Topic `orders` → Incident Intelligence Engine

Incident Intelligence Engine → Runbook Recommendation → Incident Summary

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
- Incident intelligence engine for failed orders and latency anomalies
- ML-based latency anomaly detection using Isolation Forest
- Runbook recommendation for production support scenarios
- AI-style incident summary generation

---

# Tech Stack

- Python
- FastAPI
- Kafka
- Prometheus
- Grafana
- Docker
- Kubernetes
- Scikit-learn
- NumPy

---

# API Endpoints

| Endpoint | Description |
|---|---|
| `/health` | Application health |
| `/place-order` | Generate simulated trading order |
| `/metrics` | Prometheus metrics |
| `/simulate-fix-disconnect` | Simulate FIX disconnect |
| `/simulate-fix-reconnect` | Restore FIX connection |
| `/simulate-market-data-down` | Simulate market data outage |
| `/simulate-market-data-up` | Restore market data |

---

# Prometheus Metrics

- `trading_orders_total`
- `trading_failed_orders_total`
- `trading_order_latency_seconds`
- `fix_session_status`
- `market_data_status`

---

# Incident Intelligence Engine

The Incident Intelligence Engine consumes Kafka order events and performs:

- Failed order detection
- Latency anomaly detection
- Incident classification
- Runbook recommendation
- AI-style incident summary generation

Example output:

```text
INCIDENT DETECTED:

Incident Type: Order Failure

Severity: Medium

Recommended Runbook: runbooks/order-failures.md
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
├── incident-engine
│   ├── Dockerfile
│   ├── incident_engine.py
│   └── requirements.txt
├── runbooks
│   ├── fix-disconnect.md
│   ├── high-latency.md
│   ├── market-data-down.md
│   └── order-failures.md
├── screenshots
│   ├── grafana-dashboard.png
│   ├── kafka-consumer.png
│   ├── prometheus-metrics.png
│   └── incident-engine.png
├── docs
│   └── kafka-flow.md
├── grafana
├── kafka
├── k8s
│   ├── grafana-deployment.yml
│   ├── prometheus-deployment.yml
│   ├── trading-api-deployment.yml
│   └── trading-api-service.yml
├── prometheus
│   └── prometheus.yml
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/ShaiveSharma02/trading-infrastructure-observability-platform.git
cd trading-infrastructure-observability-platform
```

---

## Start Platform

```bash
docker compose up --build
```

---

# Access URLs

| Service | URL |
|---|---|
| Trading API | http://127.0.0.1:8000 |
| Prometheus | http://127.0.0.1:9090 |
| Grafana | http://127.0.0.1:3000 |

---

# Kafka Topic

Orders are streamed to Kafka topic:

```text
orders
```

---

# Kafka Consumer Logs

```bash
docker logs -f order-consumer
```

---

# Incident Engine Logs

```bash
docker logs -f incident-engine
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

## Incident Intelligence Engine

![Incident Engine](screenshots/incident-engine.png)

---

# Kubernetes

Kubernetes deployment manifests are available in:

```text
k8s/
```

---

# Future Improvements

- Alertmanager integration
- Loki log aggregation
- Jaeger distributed tracing
- CI/CD using GitHub Actions
- Helm chart deployment
- WebSocket market data simulation
- Automated remediation workflows

---

# Author

Shaive Sharma
````
