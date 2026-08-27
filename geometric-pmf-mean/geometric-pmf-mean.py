import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    pmfi = []
    
    
    for val in k:
        # Geometric PMF formula: (1 - p)^(k-1) * p
        pmf_val = ((1 - p) ** (val - 1)) * p
        pmfi.append(float(pmf_val))
    
    # Geometric distribution ka mean = 1 / p hota hai
    mean_val = 1.0 / p
    pk=np.array(pmfi)
    
    return {
        "pmf": pk,          # Yeh list of floats hai
        "mean": float(mean_val)
    }