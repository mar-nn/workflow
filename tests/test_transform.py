import numpy as np
import pytest

from mar.nn.workflow import Transform


def _filter(datasets: dict, target):
    return list(filter(lambda ds: ds.name == target, datasets))[0]


@pytest.mark.parametrize("target", ["users", "items"])
def test_fit(schema, data, target):
    transformer = Transform(_filter(schema.datasets, target))
    transformer.fit(data)

    assert len(transformer.transformers) == len(
        _filter(schema.datasets, target).features
    )


@pytest.mark.parametrize("target", ["users", "items"])
def test_transform(schema, data, target):
    transformer = Transform(_filter(schema.datasets, target))
    ids, features = transformer.fit(data).transform(data)

    assert ids.shape == (data.shape[0], 1)
    assert len(np.unique(ids)) == data.loc[:, f"{target[:-1]}Id"].nunique()

    assert len(features.shape) == 2
    assert features.shape[0] == data.shape[0]
    assert features.shape[1] >= 1
    assert features.dtype == float


@pytest.mark.parametrize("target", ["users", "items"])
def test_call(schema, data, target):
    transformer = Transform(_filter(schema.datasets, target))
    ids, features = transformer(data)

    assert ids.shape == (data.shape[0], 1)
    assert len(np.unique(ids)) == data.loc[:, f"{target[:-1]}Id"].nunique()

    assert len(features.shape) == 2
    assert features.shape[0] == data.shape[0]
    assert features.shape[1] >= 1
    assert features.dtype == float
