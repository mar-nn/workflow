import json

import yaml
from pydantic import BaseModel


class _Feature(BaseModel):
    name: str
    type: str
    references: str | None = None


class _Dataset(BaseModel):
    name: str
    main: bool
    features: list[_Feature]


class _Model(BaseModel):
    type: str
    hyperparameters: dict = None


class Schema(BaseModel):
    datasets: list[_Dataset]
    model: _Model

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, "r") as f:
            return Schema(**yaml.safe_load(f))

    @classmethod
    def from_json(cls, path: str):
        with open(path, "r") as f:
            return Schema(**json.load(f))
