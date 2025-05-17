import numpy as np

from nupgis.ops import distance
from nupgis.validation import check_point_structure


def vertex_cluster_reduction(points: list[np.ndarray], epsilon: float) -> list[np.ndarray]:
    if not check_point_structure(points=points):
        raise ValueError("Points are invalid. Ensure all points are 2d")

    start = points[0]
    reduced: list[np.ndarray] = [start]

    for point in points[1:]:
        cur_dist = distance(x=start, y=point)
        if np.greater(cur_dist, epsilon):
            start = point
            reduced.append(point)

    return reduced
