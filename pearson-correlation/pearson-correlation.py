import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    
    if X.ndim!=2:
        return None
    if len(X)<2: 
        return None
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    A=np.dot(X_centered.T,  X_centered)
    A=A/(len(X)-1)
    std = np.sqrt(np.diag(A))

    # Step 4: Pearson correlation
    corr = A / np.outer(std, std)

    # Step 5: Handle zero variance
    zero = (std == 0)
    corr[zero, :] = np.nan
    corr[:, zero] = np.nan
    for i in range(len(std)):
        if std[i] != 0:
            corr[i, i] = 1.0
    return corr
    
    