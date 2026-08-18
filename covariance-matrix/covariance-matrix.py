import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)

    if X.ndim!=2:
        return None
    if len(X)<2:
        return None
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    A=np.dot(X_centered.T,  X_centered)
    A=A/(len(X)-1)
    return A