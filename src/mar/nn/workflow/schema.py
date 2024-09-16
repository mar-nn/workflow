import json

import yaml
from pydantic import BaseModel, RootModel


class _References(BaseModel):
    dataset: str
    field: str


class _Feature(BaseModel):
    name: str
    type: str
    references: _References | None = None


class _Dataset(BaseModel):
    name: str
    main: bool
    features: list[_Feature]


class _DatasetList(RootModel):
    root: list[_Dataset]

    def filter(self, first: bool = True, **kwargs):
        def filter_fn(ds):
            return all(getattr(ds, key) == value for key, value in kwargs.items())

        res = list(filter(filter_fn, self.root))
        return res[0] if first else res

    def __len__(self):
        return len(self.root)

    def __getitem__(self, item):
        return self.root[item]


class _Model(BaseModel):
    type: str
    hyperparameters: dict = None


class Schema(BaseModel):
    datasets: _DatasetList
    model: _Model

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, "r") as f:
            return Schema(**yaml.safe_load(f))

    @classmethod
    def from_json(cls, path: str):
        with open(path, "r") as f:
            return Schema(**json.load(f))
