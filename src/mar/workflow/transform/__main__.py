import click
import pandas as pd

from mar.workflow.transform import Transform


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
