"""
Data
=====

This module provides the :class:`.PassengersDataFrame` class, which
exposes methods for manipulating the `Titanic data`_.

.. _Titanic data: https://www.kaggle.com/c/titanic/data

"""

from __future__ import annotations

# Third Party --------------------------------------------------------------------------
from bike_sharing_demand.paths import original_test_data_path, original_train_data_path
from dotenv import load_dotenv

# Data Science
import pandas as pd


load_dotenv()


class BikeRentalDataFrame(pd.DataFrame):
    """Passengers Data Frame."""

    def __init__(self, kind: str = "train") -> None:
        if kind == "test":
            super().__init__(
                pd.read_csv(original_test_data_path(), index_col=0, parse_dates=True)
            )
        else:
            super().__init__(
                pd.read_csv(original_train_data_path(), index_col=0, parse_dates=True)
            )

    def count_column(self) -> BikeRentalDataFrame:
        return self["count"]

    @property
    def _constructor_expanddim(self) -> NotImplementedError:
        return super()._constructor_expanddim()
