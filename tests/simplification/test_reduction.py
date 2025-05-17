import pytest
from numpy import array

from nupgis.simplification.reduction import vertex_cluster_reduction


def test_vertex_cluster_reduction() -> None:
    points = [
        array([1, 2]),
        array([3, 4]),
        array([3.01, 4]),
        array([5, 3]),
        array([5, 3.01]),
    ]

    reduced = vertex_cluster_reduction(points=points, epsilon=0.1)
    assert isinstance(reduced, list)
    assert len(reduced) == 3

    with pytest.raises(ValueError):
        points[2] = array([3.01, 4, 5])
        _ = vertex_cluster_reduction(points=points, epsilon=0.1)
