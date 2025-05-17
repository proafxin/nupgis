import pytest

import numpy as np
from nupgis.ops import distance

def test_distance() -> None:
    x = np.array([1,2])
    y = np.array([3,4])

    dist = distance(x=x, y=y)
    assert isinstance(dist, float)
