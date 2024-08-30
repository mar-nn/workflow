import pytest
import os
import pandas as pd
import yaml


FIXTURES_PATH = os.path.join("tests", "fixtures")


@pytest.fixture
def schema():
    schema_path = os.path.join(FIXTURES_PATH, "schema.yaml")
    with open(schema_path, "r") as f:
        return yaml.safe_load(f)


@pytest.fixture
def data():
    data_path = os.path.join(FIXTURES_PATH, "data.csv")
    return pd.read_csv(data_path)
