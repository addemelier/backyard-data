# Backyard Data

Seattle's permitting rules are long, dense, and hard to interpret — especially when you're trying to figure out what you can actually build in your backyard. The permit dataset tells a clearer story: what people applied for, what got approved, how long it took, and what it cost.

This project builds a data pipeline over Seattle's public building permits dataset to answer practical questions about accessory dwelling units (ADUs): what gets built, where, and under what conditions. The end result is a public tool anyone can use to explore the data themselves.

## What it does

- Ingests the [Seattle Building Permits dataset](https://data.seattle.gov/Permitting/Building-Permits/76t5-zqzr) via the Socrata API
- Models and transforms the data with dbt
- Monitors pipeline health with automated data quality checks
- Uses AI agents to detect anomalies and attempt self-healing when things go wrong
- Exposes a public Streamlit app for exploring ADU permit trends

## Architecture

> Architecture diagram coming soon.

| Layer | Tool |
|---|---|
| Ingestion | Python + Socrata API |
| Storage | PostgreSQL |
| Transformation | dbt |
| Observability | dbt tests + custom checks |
| Agent loop | Claude API |
| Frontend | Streamlit |

## Running locally

This project uses [uv](https://docs.astral.sh/uv/) for Python dependency management.

```bash
# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repo
git clone https://github.com/addemelier/backyard-data.git
cd backyard-data

# Create virtual environment and install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Fill in .env with your values
```

> Dependencies will be added to pyproject.toml as the project grows.

## Security

**Reporting a vulnerability:** Open a GitHub issue with the label `security`. Do not include secret values in issue text.

**If a secret is accidentally committed:** Rotate it immediately — git history cannot be trusted even after a revert. Then remove the secret from history using `git filter-repo`.

**Running security checks locally:**
```bash
# Scan for secrets
uvx detect-secrets scan

# Audit Python dependencies for known CVEs
uvx pip-audit
```

This repo uses [GitHub secret scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning) (enabled in repo settings), [Dependabot](https://docs.github.com/en/code-security/dependabot) for automated dependency updates, and `pip-audit` in CI on every PR.

## Follow along

This project is documented on Substack as it's built. [Link coming soon.]
