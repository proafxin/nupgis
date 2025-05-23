from typing import Sequence

from numpy import array

from nupgis.simplification.lang import simplify_polygon


def test_douglas_peucker() -> None:
    points = [array([1, 3]), array([2, 4]), array([2, 4.05]), array([2.01, 4.07]), array([6, 3]), array([7, 4])]

    reduced = simplify_polygon(points=points)

    assert isinstance(reduced, Sequence)
    assert len(reduced) == 6
    points[2] = array([2, 4])
    reduced = simplify_polygon(points=points)
    assert len(reduced) == 5
    reduced = simplify_polygon(points=points[:2])
    assert len(reduced) == len(points[:2])
