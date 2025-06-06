from collections.abc import Sequence

import numpy as np

from nupgis.smoothing.sliding_average import mcmaster


def test_mcmaster(polygon: np.ndarray) -> None:
    smoothed_polygons = mcmaster(polygons=[polygon, np.array([[0, 1], [1, 0]])], look_ahead=1)
    smoothed_polygons = mcmaster(polygons=[np.array([[0, 1]])], look_ahead=3)
    smoothed_polygons = mcmaster(polygons=[polygon, np.array([[0, 1], [1, 0]])], look_ahead=3)

    assert isinstance(smoothed_polygons, Sequence)
    for smoothed_polygon in smoothed_polygons:
        assert isinstance(smoothed_polygon, np.ndarray)
        assert smoothed_polygon.shape[1] == 2

    smoothed_polygons = mcmaster(
        polygons=[polygon, np.array([[0, 0], [0, 1], [1, 0], [0, 0]])], look_ahead=3
    )
    assert isinstance(smoothed_polygons, Sequence)
