.PHONY: dev db db-stop reset seed test lint

# Start local database and Dagster UI
dev: db
	uv run dagster dev

# Start local database only
db:
	docker compose up -d --wait

# Stop local database (keeps data)
db-stop:
	docker compose down

# Wipe and restart database, then reload seed data
reset:
	docker compose down -v
	docker compose up -d
	$(MAKE) seed

# Load seed fixture data into local Postgres
seed:
	uv run python scripts/seed.py

# Run tests
test:
	uv run pytest

# Lint Python
lint:
	uv run ruff check .
