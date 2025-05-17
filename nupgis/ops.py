import numpy as np


def distance(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.linalg.norm(x - y))
