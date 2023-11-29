#!/usr/bin/python3
"""Function definition of a matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The fist matrix.
        m_b (lists of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
