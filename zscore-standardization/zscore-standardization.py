import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    x = np.asarray(X, dtype=float)

    mean = np.mean(x, axis=axis, keepdims=True)
    std = np.std(x, axis=axis, keepdims=True)

    # Initialize result with zeros
    result = np.zeros_like(x)

    # Perform division only where std > eps
    np.divide(x - mean, std, out=result, where=std > eps)

    return result