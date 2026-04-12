from datetime import datetime, timezone

from dagster import asset


@asset
def smoke_test(context) -> str:
    """Heartbeat asset. Proves the pipeline plumbing works end to end."""
    timestamp = datetime.now(timezone.utc).isoformat()
    context.log.info(f"Smoke test heartbeat: {timestamp}")
    return timestamp
