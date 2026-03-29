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

```bash
# Clone the repo
git clone https://github.com/addemelier/backyard-data.git
cd backyard-data

# Set up environment
cp .env.example .env
# Fill in .env with your values

# Install dependencies
pip install -r requirements.txt
```

> Full setup instructions will be added as the project matures.

## Follow along

This project is documented on Substack as it's built. [Link coming soon.]
