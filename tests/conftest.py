import pytest
import os
import pandas as pd

from mar.nn.workflow.schema import Schema


FIXTURES_PATH = os.path.join("tests", "fixtures")


@pytest.fixture
def schema():
    schema_path = os.path.join(FIXTURES_PATH, "schema.yaml")
    return Schema.from_yaml(schema_path)


@pytest.fixture
def data():
    data_path = os.path.join(FIXTURES_PATH, "data.csv")
    return pd.read_csv(data_path)
