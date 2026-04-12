from dagster import AssetSelection, ScheduleDefinition, define_asset_job

# Runs daily at 6am UTC — comfortable buffer after Seattle Open Data refreshes overnight
daily_job = define_asset_job(
    name="daily_pipeline",
    selection=AssetSelection.all(),
)

daily_schedule = ScheduleDefinition(
    job=daily_job,
    cron_schedule="0 6 * * *",
)
