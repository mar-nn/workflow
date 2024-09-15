import pytest
from pydantic import ValidationError

from mar.nn.workflow.schema import Schema


def test_init():
    datasets = [
        {
            "name": "interactions",
            "main": "true",
            "features": [{"name": "foo", "type": "id"}],
        }
    ]
    model = {"type": "test"}
    schema = Schema(datasets=datasets, model=model)

    assert len(schema.datasets) == 1
    assert schema.datasets[0].name == "interactions"
    assert schema.model.type == "test"
    assert schema.model.hyperparameters is None


def test_init_no_interactions():
    with pytest.raises(ValidationError):
        Schema(datasets=None, model={"type": "foo"})


def test_init_no_model_type():
    with pytest.raises(ValidationError):
        Schema(datasets={"interactions": {"foo": "bar"}}, model=None)


def test_from_yaml():
    Schema.from_yaml("tests/fixtures/schema.yaml")


def test_from_json():
    Schema.from_json("tests/fixtures/schema.json")
