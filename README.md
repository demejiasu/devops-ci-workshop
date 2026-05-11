# DevOps CI Workshop

![CI/CD](https://github.com/cesarpalacios/devops-ci-workshop/actions/workflows/ci.yml/badge.svg)

Repositorio base para el taller de CI/CD con GitHub Actions + Observabilidad.

## Endpoints

| Endpoint | Descripción |
|----------|-------------|
| `/` | Status del servicio |
| `/health` | Health check con métricas de sistema |
| `/metrics` | Métricas en formato Prometheus |

## Ejecutar localmente

```bash
pip install -r requirements.txt
python app.py
```

## Ejecutar con Docker

```bash
docker build -t devops-api .
docker run -p 5000:5000 devops-api
```

## Ejecutar con Docker Compose (API + Prometheus)

```bash
docker compose up -d
```

- API: http://localhost:5000
- Prometheus: http://localhost:9090

## Tests

```bash
pytest test_app.py -v
```

---

*DevOps — UNAL Sede Manizales — 2026-1*
