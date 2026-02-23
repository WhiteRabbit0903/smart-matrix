import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Multiply two matrices using NumPy.

    Parameters
    ----------
    A : np.ndarray
        First matrix
    B : np.ndarray
        Second matrix

    Returns
    -------
    np.ndarray
        Result of matrix multiplication
    """
    return np.dot(A, B)


def matrix_transpose(A: np.ndarray) -> np.ndarray:
    """
    Transpose matrix.
    """
    return A.T

