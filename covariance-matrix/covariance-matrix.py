import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X=np.array(X,dtype=float)
    mean=np.mean(X,axis=0)
    print(mean)
    cov=((X-mean).T@(X-mean))/(X.shape[0]-1)
    return cov
    