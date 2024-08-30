import pytest
import numpy as np

from mar.nn.workflow import Transform


@pytest.mark.parametrize("target", ["user", "item"])
def test_fit(schema, data, target):
    transformer = Transform(schema["transform"]["data"][target])
    transformer.fit(data)

    assert len(transformer.transformers) == len(schema["transform"]["data"][target])


@pytest.mark.parametrize("target", ["user", "item"])
def test_transform(schema, data, target):
    transformer = Transform(schema["transform"]["data"][target])
    ids, features = transformer.fit(data).transform(data)

    assert ids.shape == (data.shape[0], 1)
    assert len(np.unique(ids)) == data.loc[:, f"{target}Id"].nunique()

    assert len(features.shape) == 2
    assert features.shape[0] == data.shape[0]
    assert features.shape[1] >= 1
    assert features.dtype == float
