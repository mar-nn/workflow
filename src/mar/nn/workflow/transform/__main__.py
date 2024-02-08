import pandas as pd


def transform(data: str, schema: str, format: str, **options):
    data: pd.DataFrame = getattr(pd, f"read_{format}")(data)
    return data


if __name__ == "__main__":
    transform()
