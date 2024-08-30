import json

import yaml
from pydantic import BaseModel


class _Datasets(BaseModel):
    interactions: dict
    users: dict = None
    items: dict = None


class _Model(BaseModel):
    type: str
    hyperparameters: dict = None


class Schema(BaseModel):
    datasets: _Datasets
    model: _Model

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, "r") as f:
            return Schema(**yaml.safe_load(f))

    @classmethod
    def from_json(cls, path: str):
        with open(path, "r") as f:
            return Schema(**json.load(f))
