# SelfLink Backend

This directory contains the Django/DRF backend for the SelfLink platform. The
architecture follows the blueprint in `SelfLink_Project_Blueprint.txt`,
providing a modular monorepo layout where each domain lives under `apps/` and
shared utilities live under `libs/`.

## Quickstart

```bash
python3 -m pip install --user -r requirements/dev.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Visit `http://localhost:8000/health/` for a readiness check and
`http://localhost:8000/api/docs/` for the interactive API documentation.

## Settings

Settings are split into `core/settings/base.py`, `dev.py`, and `prod.py`. Set
`DJANGO_SETTINGS_MODULE=core.settings.prod` for production deployments.

Environment variables can be stored in `selflink/.env`. See the project
blueprint for the full list of services and future milestones.
