import numpy as np


def check_point_structure(points: list[np.ndarray]) -> bool:
    if len(points) < 1:
        raise ValueError("Empty list of points")

    for point in points:
        if not isinstance(point, np.ndarray):
            raise ValueError("Every point must be a numpy array")

        if point.ndim != 1 or len(point.shape) > 1 or point.shape[0] != 2:
            return False

    return True
