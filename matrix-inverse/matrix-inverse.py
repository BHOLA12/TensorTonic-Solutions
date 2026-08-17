import numpy as np

def matrix_inverse(A):
    A = np.array(A)

    if A.shape[0] != A.shape[1] or np.isclose(np.linalg.det(A), 0):
        return None

    return np.linalg.inv(A)