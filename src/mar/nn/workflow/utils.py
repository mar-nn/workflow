def filter_schema(datasets: list, target: str):
    return list(filter(lambda ds: ds.name == target, datasets))[0]
