from pydantic import BaseModel


class DatasetsConfig(BaseModel):
    interactions: dict
    users: dict = None
    items: dict = None


class ModelConfig(BaseModel):
    type: str
    hyperparameters: dict


class Schema(BaseModel):
    datasets: DatasetsConfig
    model: dict
