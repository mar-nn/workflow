import click
import pandas as pd


@click.command
@click.option("--data")
@click.option("--schema")
@click.option("--format")
def transform(data: str, schema: str, format: str):
    data: pd.DataFrame = getattr(pd, f"read_{format}")(data)
    return data


if __name__ == "__main__":
    transform()
