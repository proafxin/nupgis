from typing import Sequence

from numpy import array

from nupgis.simplification.douglas_peucker import simplify_polygon


def test_douglas_peucker() -> None:
    points = [array([1, 3]), array([2, 4]), array([2, 4.05]), array([2.01, 4.07]), array([6, 3]), array([7, 4])]

    reduced = simplify_polygon(points=points, epsilon=0.1)

    assert isinstance(reduced, Sequence)
    assert len(reduced) == 4
    reduced = simplify_polygon(points=points, epsilon=100)
    assert isinstance(reduced, Sequence)
    assert len(reduced) == 2
