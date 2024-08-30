import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer

from .features import CategoryEncoder, IDEncoder, NumberEncoder


_ENCODER_MAPPING = {
    "category": CategoryEncoder,
    "number": NumberEncoder,
    "id": IDEncoder,
}


class Transform(ColumnTransformer):
    _feature_index: dict[str, list[int]]

    def __init__(self, schema):
        super().__init__(transformers=[], remainder="drop")
        self.schema = schema

    def __call__(self, X: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        return self.fit(X).transform(X)

    def fit(self, X: pd.DataFrame):
        feature_index = self._get_feature_indices(self.schema, X.columns.values)
        self.transformers = self._get_transformers(feature_index)
        return super().fit(X.values)

    def transform(self, X) -> tuple[np.ndarray, np.ndarray]:
        transformed: np.ndarray = super().transform(X.values)
        return transformed[:, -1:], transformed[:, :-1]

    @staticmethod
    def _get_transformers(index_dict: dict[str, list]) -> list[tuple]:
        return [
            tuple(_ENCODER_MAPPING[feature_type](index))
            for feature_type, index in index_dict.items()
            if len(index) > 0
        ]

    @staticmethod
    def _get_feature_indices(
        schema: dict[str, str], header: np.ndarray
    ) -> dict[str, list[int]]:
        idx = {feature_type: [] for feature_type in _ENCODER_MAPPING.keys()}
        for feature, feature_type in schema.items():
            idx[feature_type] += np.where(header == feature)[0].tolist()
        return idx
