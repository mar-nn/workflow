import os
import click
import numpy as np
import pandas as pd
from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, PointStruct

from mar.workflow.transform import Transform

QDRANT_URL = os.environ["QDRANT_URL"]
QDRANT_PORT = os.environ["QDRANT_PORT"]

qdrant = QdrantClient(url=QDRANT_URL, port=QDRANT_PORT)


def create_collection(size: int):
    name = str(uuid4())
    config = VectorParams(size=size)
    qdrant.create_collection(name, config)
    return name


def get_points(ids: np.ndarray, vectors: np.ndarray):
    ids = ids.reshape(-1)
    vectors = vectors.tolist()
    return [PointStruct(id=int(id), vector=vector) for id, vector in zip(ids, vectors)]


@click.command
@click.option("--data")
@click.option("--schema")
@click.option("--format")
def transform(data: str, schema: str, format: str = "csv"):
    data: pd.DataFrame = getattr(pd, f"read_{format}")(data)
    ids, vectors = Transform(schema)(data)
    name = create_collection(size=vectors.shape[1])
    points = get_points(ids, vectors)
    qdrant.upsert(name, points)


if __name__ == "__main__":
    transform()
