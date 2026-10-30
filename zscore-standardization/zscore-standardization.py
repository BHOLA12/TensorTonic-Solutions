def zscore_standardize(
    X: list, axis: int = 0, eps: float = 1e-12
) -> np.ndarray:
    x = np.asarray(X, dtype=float)

    mean = np.mean(x, axis=axis, keepdims=True)
    std = np.std(x, axis=axis, keepdims=True)
    safe_std = np.maximum(std, eps)

    return (x - mean) / safe_std