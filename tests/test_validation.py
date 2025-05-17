import numpy as np
import pytest

from nupgis.validation import check_point_structure


def test_point_structure() -> None:
    points = [np.array([1, 2]), np.array([3, 4])]

    status = check_point_structure(points=points)
    assert status is True

    with pytest.raises(ValueError):
        _ = check_point_structure(points=[])

    with pytest.raises(ValueError):
        _ = check_point_structure(points=[[1, 2], [3, 4]])  # type: ignore [list-item]

    points[1] = np.array([3, 4, 5])
    status = check_point_structure(points=points)
    assert status is False
