import os

import click
import pandas as pd

from mar.nn.workflow import Transform
from mar.nn.workflow.schema import Schema
from mar.nn.workflow.utils import filter_schema


@click.command
@click.option("--data", "-d")
@click.option("--schema", "-s")
@click.option("--target", "-t")
@click.option("--output", "-o")
@click.option("--format", "-f", default="csv")
def transform(data: str, schema: str, target: str, output: str, format: str = "csv"):
    data = getattr(pd, f"read_{format}")(data)
    schema = Schema.from_yaml(schema)
    schema = filter_schema(schema.datasets, target)

    transform = Transform(schema)
    X = transform(data)

    transformer_path = os.path.join(output, "transformer", "transform.pkl")
    data_path = os.path.join(output, "data", "transform.pq")

    transform.save(transformer_path)
    X.to_parquet(data_path)
