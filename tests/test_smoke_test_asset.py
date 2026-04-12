from dagster import materialize

from backyard_data.assets.smoke_test import smoke_test


def test_smoke_test_asset():
    result = materialize([smoke_test])
    assert result.success
    output = result.output_for_node("smoke_test")
    assert isinstance(output, str)
    assert "T" in output  # ISO 8601 timestamp contains "T"
