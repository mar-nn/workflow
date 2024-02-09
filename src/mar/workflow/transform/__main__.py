import os
import click
import pandas as pd

from qdrant_client import QdrantClient

from mar.workflow.transform import Transform

QDRANT_URL = os.environ["QDRANT_URL"]
QDRANT_PORT = os.environ["QDRANT_PORT"]

qdrant = QdrantClient(url=QDRANT_URL, port=QDRANT_PORT)


@click.command
@click.option("--data")
@click.option("--schema")
@click.option("--format")
@click.option("--target")
def transform(data: str, schema: str, format: str = None):
    data: pd.DataFrame = getattr(pd, f"read_{format}")(data)
    ids, vectors = Transform(schema)(data)


if __name__ == "__main__":
    transform()
