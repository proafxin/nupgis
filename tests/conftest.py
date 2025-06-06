import numpy as np
import pytest


@pytest.fixture
def polygon() -> np.ndarray:
    return np.array([[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [1, 2], [1, 1], [0, 1], [0, 0]])
