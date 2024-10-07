import os

import click
import pandas as pd

from mar.workflow import Transform
from mar.workflow.schema import Schema


@click.command
@click.option("--data", "-d")
@click.option("--schema", "-s")
@click.option("--target", "-t")
@click.option("--output", "-o")
@click.option("--format", "-f", default="csv")
def transform(data: str, schema: str, target: str, output: str, format: str = "csv"):
    data = getattr(pd, f"read_{format}")(data)
    schema = Schema.from_yaml(schema)

    transform = Transform(schema.filter_datasets(target))
    X = transform(data)

    transformer_path = os.path.join(output, "transformer", "transform.pkl")
    data_path = os.path.join(output, "data", "transform.pq")

    transform.save(transformer_path)
    X.to_parquet(data_path)
