import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    x=np.asarray(X,dtype=float)
    mean=np.mean(x,axis=0)
    
    cov=(x-mean).T@(x-mean)/(x.shape[0]-1)
    std = np.std(x, axis=0, ddof=1)
    denominator = np.outer(std, std)
    resi = np.full_like(cov, np.nan, dtype=float)
    for i in range(cov.shape[0]):
        for j in range(cov.shape[1]):
            if denominator[i][j]!=0:
               
              resi[i][j]=cov[i][j]/denominator[i][j]
            
    
    return resi