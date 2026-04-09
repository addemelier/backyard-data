# Environments

## Overview

| Environment | Database | Who runs it |
|---|---|---|
| `local` | Docker Postgres + PostGIS | Developer (you) |
| `production` | Supabase | Dagster Cloud (pipeline), Vercel (frontend) |

The core rule: **Dagster only ever writes to production. Local dev never touches prod data.**

---

## Local development

### Start the database

```bash
docker compose up -d
```

This starts a Postgres 15 + PostGIS instance on `localhost:5432`. Data persists in a named Docker volume (`pgdata`) between restarts.

### Environment variables

Copy `.env.example` to `.env.local` and fill in your values:

```bash
cp .env.example .env.local
```

The local `DATABASE_URL` is pre-filled to point at the Docker container — no changes needed for basic dev.

### Stop the database

```bash
docker compose down       # stop, keep data
docker compose down -v    # stop and wipe data (fresh start)
```

---

## Production

Production uses [Supabase](https://supabase.com) as the managed Postgres host with PostGIS enabled.

Secrets are injected at runtime — never stored in the repo:
- **Dagster Cloud** — env vars set in the Dagster Cloud project settings UI
- **Vercel** — env vars set in the Vercel project settings UI (prod values for production, placeholder/dev values for preview deployments)

---

## Adding a new secret

1. Add it to `.env.example` with a comment explaining what it's for and where to get it
2. Add it to your local `.env.local`
3. Add it to Dagster Cloud settings (if the pipeline needs it)
4. Add it to Vercel settings (if the frontend needs it)
5. Add it as a GitHub Actions secret (if CI needs it)

Never hardcode secrets. Never commit `.env.local` or `.env.production`.

---

## Environment variable reference

| Variable | Used by | Where to get it |
|---|---|---|
| `APP_ENV` | All | Set to `local` or `production` |
| `DATABASE_URL` | Pipeline, dbt | Docker locally; Supabase in prod |
| `SUPABASE_URL` | Frontend, pipeline | Supabase project settings |
| `SUPABASE_KEY` | Frontend, pipeline | Supabase project settings → API |
| `SOCRATA_APP_TOKEN` | Ingestion | data.seattle.gov developer portal |
| `DAGSTER_CLOUD_API_TOKEN` | CI/CD | Dagster Cloud → user settings |
| `MAPBOX_TOKEN` | Frontend | mapbox.com → account → tokens |
