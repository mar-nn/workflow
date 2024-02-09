import string
import numpy as np
import pandas as pd

from mar.workflow.transform import Transform


data = pd.DataFrame(
    {
        "user_id": np.random.choice(list(string.ascii_lowercase), size=1000),
        "age": np.random.choice(100, size=1000),
        "gender": np.random.choice(["m", "f"], size=1000),
    }
)

schema = {"user_id": "id", "age": "number", "gender": "category"}


def test_fit():
    feat = Transform(schema)
    feat.fit(data)


def test_transform():
    transform = Transform(schema)
    transformed_data = transform(data)
    ids, feats = transformed_data
    assert ids.shape == (data.shape[0], 1)
    assert feats.shape == (data.shape[0], 3)
