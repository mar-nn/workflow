import click
import pandas as pd

from mar.nn.workflow.schema import Schema


@click.command
@click.option("--data", "-d")
@click.option("--schema", "-s")
@click.option("--format", "-f", default="csv")
def transform(data: str, schema: str, format: str = "csv"):
    data = getattr(pd, f"read_{format}")(data)
    schema = Schema.from_yaml(schema)
