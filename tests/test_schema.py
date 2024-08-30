from mar.nn.workflow.schema import Schema


def test_from_yaml():
    Schema.from_yaml("tests/fixtures/schema.yaml")


def test_from_json():
    Schema.from_json("tests/fixtures/schema.json")
