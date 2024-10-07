import numpy as np
import pytest

from mar.workflow import Transform


@pytest.mark.parametrize("target", ["users", "items"])
def test_fit(schema, data, target):
    transformer = Transform(schema.datasets.filter(name=target))
    transformer.fit(data)

    assert len(transformer.transformers) == len(
        schema.datasets.filter(name=target).features
    )


@pytest.mark.parametrize("target", ["users", "items"])
def test_transform(schema, data, target):
    transformer = Transform(schema.datasets.filter(name=target))
    ids, features = transformer.fit(data).transform(data)

    assert ids.shape == (data.shape[0], 1)
    assert len(np.unique(ids)) == data.loc[:, f"{target[:-1]}Id"].nunique()

    assert len(features.shape) == 2
    assert features.shape[0] == data.shape[0]
    assert features.shape[1] >= 1
    assert features.dtype == float


@pytest.mark.parametrize("target", ["users", "items"])
def test_call(schema, data, target):
    transformer = Transform(schema.datasets.filter(name=target))
    ids, features = transformer(data)

    assert ids.shape == (data.shape[0], 1)
    assert len(np.unique(ids)) == data.loc[:, f"{target[:-1]}Id"].nunique()

    assert len(features.shape) == 2
    assert features.shape[0] == data.shape[0]
    assert features.shape[1] >= 1
    assert features.dtype == float
