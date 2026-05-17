FROM python:3.14-slim

WORKDIR /incident-engine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY incident_engine.py .

CMD ["python", "incident_engine.py"]