"""
Utilities
=========
"""

# Standard Library ---------------------------------------------------------------------
import functools
from typing import List

# Data Science
import numpy as np


def bump_function(x: float, mean: float = 0, radius: float = 1) -> float:
    """Return image of an *RBF* bump function with given mean and radius.

    .. math::
        \\phi_{\\mu, \\epsilon}(x) = \\begin{cases}
                    \\exp\\left(-\\frac{1}{1-\\epsilon(x - \\mu)^2}\\right)
            & \\mbox{ for } x<\\epsilon + \\mu \\\\
            0 & \\mbox{ otherwise }
        \\end{cases}

    .. image::  ./bump_function.png
        :alt: Bump Function
        :align: center
        :scale: 60%

    Parameters
    ----------
    x
        Argument.
    mean
        Mean parameter :math:`\\mu` of the bump function.
    radius
        Radius parameter :math:`\\epsilon` of the bump function.

    Returns
    -------
    :code:`float`
        Image of the bump function for provided argument and parameters.

    References
    ----------

    - https://en.wikipedia.org/wiki/Bump_function
    - https://en.wikipedia.org/wiki/Radial_basis_function
    """
    distance = abs(x - mean)

    if distance < radius:
        return bump_function_distance(distance, radius)
    else:
        return 0


@functools.lru_cache()
def bump_function_distance(distance, radius: float = 1):
    """Intermediate step for memoization.

    Parameters
    ----------
    distance
        Distance from the mean of the bump function.
    radius
        Radius parameter :math:`\\epsilon` of the bump function.

    Returns
    -------
    :code:`float`
        Image of the bump function for provided argument and parameters.
    """
    if distance < radius:
        return np.exp(1 / ((1 / radius * distance) ** 2 - 1))
    else:
        return 0


def bump_dummies(dummy_variables_list: List[int], radius: float = 0) -> List[float]:
    """Apply *RBF* bump functions on list of dummy variables.

    A bump function is applied for every non-zero entry (taking its index as
    the mean), the results are summed.

    .. image::  ./bump_dummy.png
        :alt: Bump Function
        :align: center
        :scale: 60%

    Parameters
    ----------
    dummy_variables_list
        List of dummy variables.
    radius
        Radius parameter :math:`\\epsilon` of the bump functions.

    Returns
    -------
    :code:`List[float]`
        Transformed list.
    """
    dummy_indices = np.nonzero(dummy_variables_list)[0]

    return [
        sum(
            map(
                lambda dummy_index: bump_function(i, dummy_index, radius),
                dummy_indices,
            )
        )
        for i in range(len(dummy_variables_list))
    ]
