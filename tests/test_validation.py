import numpy as np
import pytest

from nupgis.validation import validate_2d_polygon


def test_point_structure() -> None:
    points = [np.array([1, 2]), np.array([3, 4])]

    validate_2d_polygon(points=points)
    with pytest.raises(TypeError):
        validate_2d_polygon(points=reversed(points))  # type: ignore[arg-type]

    with pytest.raises(ValueError):
        validate_2d_polygon(points=[])

    with pytest.raises(ValueError):
        validate_2d_polygon(points=[[1, 2], [3, 4]])  # type: ignore [list-item]

    points[1] = np.array([3, 4, 5])
    with pytest.raises(ValueError):
        validate_2d_polygon(points=points)

    points[1] = np.array([np.nan, np.nan])
    with pytest.raises(ValueError):
        validate_2d_polygon(points=points)

    points[1] = np.array([np.inf, 2])
    with pytest.raises(ValueError):
        validate_2d_polygon(points=points)
