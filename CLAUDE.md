# Claude Code Guide — Backyard Data

## Project overview

Backyard Data is a public data engineering showcase project. It builds a data pipeline over Seattle's open building permits dataset to answer practical questions about accessory dwelling units (ADUs): what gets built, where, and how long it takes.

The end product is an interactive map (Zillow-style) where anyone can explore permit history for their neighbourhood.

**Two purposes:**
1. Staff-level data engineering portfolio — every decision is explainable and citeable
2. Answer a real personal question: what are people actually building in Seattle backyards?

## Architecture

### Two pipelines

**Pipeline 1 — Permit data ingestion (primary showcase)**
Seattle Building Permits → Socrata API → Python ingestion → Postgres (Supabase) → dbt → map UI

**Pipeline 2 — User interaction tracking**
Map UI events → backend → Postgres → analytics

### Stack

| Layer | Tool |
|---|---|
| Orchestration | Dagster (local dev) / Dagster Cloud (prod) |
| Storage | Docker Postgres + PostGIS (local) / Supabase (prod) |
| Transformation | dbt-core + dbt-postgres |
| Ingestion | Python + Socrata API |
| Observability | dbt tests + custom quality checks |
| Agent loop | Claude API |
| Frontend | Next.js + Mapbox |
| CI | GitHub Actions |

### Environments

- **Local:** Docker Postgres on `localhost:5432`, `dagster dev` runs natively
- **Production:** Supabase (Postgres + PostGIS), Dagster Cloud, Vercel

See `docs/environments.md` for the full switching convention.

## Folder structure

```
backyard-data/
├── dagster/        # Dagster asset definitions, resources, schedules, sensors
├── dbt/            # dbt project — staging, intermediate, marts models
├── notebooks/      # Exploratory analysis (not linted, not part of pipeline)
├── scripts/        # One-off utilities and backfill jobs
├── docs/           # Architecture, data dictionary, decision log, ADRs
├── tests/          # pytest tests for pipeline code
├── .github/        # CI workflows and Dependabot config
└── docker-compose.yml  # Local Postgres + PostGIS
```

## Running locally

```bash
# Start the local database
docker compose up -d

# Install dependencies
uv sync

# Run tests
uv run pytest

# Lint Python
uv run ruff check .

# Start Dagster UI
uv run dagster dev
```

## Python / package management

This project uses [uv](https://docs.astral.sh/uv/). Always use uv commands — never call `pip` or `python` directly.

| Instead of | Use |
|---|---|
| `pip install <pkg>` | `uv add <pkg>` |
| `pip install -r requirements.txt` | `uv sync` |
| `python script.py` | `uv run script.py` |
| `python -m pytest` | `uv run pytest` |

## Conventions

- **Python:** ruff for linting and formatting. Notebooks are excluded from linting.
- **SQL:** sqlfluff with dbt dialect. Models follow staging → intermediate → marts naming.
- **Secrets:** Never committed. `.env.local` for local dev, injected via Dagster Cloud / Vercel in prod.
- **Branches:** `ad/<feature-name>` — PRs required to merge to main.
- **Commits:** Conventional commits (`feat:`, `fix:`, `chore:`, etc.).
- **Dagster rule:** Dagster only ever writes to production Supabase. Local dev uses the Docker Postgres.

## Notion task board

This project is tracked in Notion. Use the Notion MCP integration to read and update tasks as you work.

**Finding tasks:**
- Search Notion for "Backyard Data" to locate the project page and tasks database
- From there you can find individual tasks by name using `notion-search`

**Two separate Notion databases:**
- **Tasks** (`collection://d8fadfd5-544b-83e9-92cb-07ec8a8a1832`) — individual units of work within a project. Status values: `Not started`, `In progress`, `Done`
- **Projects** (`collection://f22adfd5-544b-83c4-94a7-875f3f68a725`) — epics that group multiple tasks. Status values: `Planning`, `In progress`, `Done`

**Workflow:**
1. Fetch the relevant task from Notion before starting work
2. Set the **task** status to `In progress` when you begin; set the **project** status to `In progress` when you start the first task in it
3. Mark individual **tasks** as `Done` as they are completed — no review needed
4. **Before marking a *project* as `Done`** (i.e. before calling `notion-update-page` on a page from the Projects database with `Status: Done`), you MUST perform an epic review:
   - Read the codebase changes made during the epic
   - Review through three lenses: staff data engineer, staff security engineer, staff frontend engineer (see `.claude/commands/` for each persona's focus areas)
   - For each high-priority concern found, create a new task in the Tasks database with status `Not started` and priority `High`
   - Low-priority concerns can be noted but do not need tickets
   - Only then mark the project `Done`
