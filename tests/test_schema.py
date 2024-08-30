import pytest
from pydantic import ValidationError

from mar.nn.workflow.schema import Schema


def test_init():
    schema = Schema(datasets={"interactions": {"foo": "bar"}}, model={"type": "test"})

    assert schema.datasets.interactions == {"foo": "bar"}
    assert schema.model.type == "test"
    assert schema.datasets.users is None
    assert schema.datasets.items is None
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
