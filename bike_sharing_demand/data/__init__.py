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
from bike_sharing_demand.utilities import bump_dummies
from dotenv import load_dotenv

# Data Science
import pandas as pd


load_dotenv()


class BikeRentalDataFrame(pd.DataFrame):
    """Passengers Data Frame."""

    # Ignoring "casual" and "registered" as not present in the test data.
    # Ignoring "season" as redundant.
    used_columns = [
        "datetime",
        "holiday",
        "workingday",
        "weather",
        "temp",
        "atemp",
        "humidity",
        "windspeed",
    ]
    prediction_column = ["count"]

    def __init__(self, kind: str = "train") -> None:
        if kind == "test":
            super().__init__(
                pd.read_csv(
                    original_test_data_path(),
                    index_col=0,
                    parse_dates=True,
                    usecols=self.used_columns,
                )
            )
        else:
            super().__init__(
                pd.read_csv(
                    original_train_data_path(),
                    index_col=0,
                    parse_dates=True,
                    usecols=self.used_columns + self.prediction_column,
                )
            )

    def count_column(self) -> BikeRentalDataFrame:
        return self["count"]

    def bump_hours(self) -> BikeRentalDataFrame:
        """
        warnings: not quite optimized, long operation long operation
        Returns
        -------

        """
        dummies = pd.get_dummies(self.index.hour, prefix="rbf_hour")

        bumped_dummies = dummies.apply(
            lambda row: bump_dummies(row, radius=1.5), raw=True
        )

        return self.append(bumped_dummies)

    @property
    def _constructor_expanddim(self) -> NotImplementedError:
        return super()._constructor_expanddim()


def save_bumped_hour_dummies(file_name="bumped_hour_dummies")

print("adsf")

df = BikeRentalDataFrame().bump_hours()

print(df)
