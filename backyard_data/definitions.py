from dagster import Definitions, load_assets_from_package_module

from backyard_data import assets
from backyard_data.schedules import daily_schedule

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    schedules=[daily_schedule],
)
