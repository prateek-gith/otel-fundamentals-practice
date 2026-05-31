# FastAPI OpenTelemetry App

This repository contains a sample FastAPI application instrumented with OpenTelemetry, PostgreSQL, Prometheus, Grafana, Loki, and Jaeger.

## Repository Structure

- `main.py` — root application entrypoint
- `app/` — Python package containing database, models, CRUD logic, telemetry, and routers
- `Dockerfile` — container image build definition
- `docker-compose.yml` — local development stack for app, PostgreSQL, OpenTelemetry collector, Prometheus, Grafana, Loki, and Jaeger
- `otel-collector-config.yaml`, `prometheus.yml`, `promtail-config.yaml` — deployment config files
- `.env` — local environment values (ignored by git)
- `.env.example` — sample environment file

## Getting Started

### Clone repository

```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd OpenTelementry
```

### Create `.env`

Copy the sample environment file and update values as needed:

```bash
copy .env.example .env
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run locally

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Docker Compose

Start the full stack with:

```bash
docker compose down                          
docker compose build --no-cache
docker compose up -d     
```

## Environment Variables

The sample file includes:

- `DATABASE_URL` — SQLAlchemy database connection string
- `SERVICE_NAME` — OpenTelemetry service name

## Notes

- Keep `.env` out of source control.
- If you use a virtual environment, avoid committing `myvenv/` by keeping it in `.gitignore`.
