import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    x=np.array(X)
    y=np.array(y)
    A=(x.T)@x
    Y=(x.T)@y
    w=(np.linalg.solve(A, Y))
    return (w)
    