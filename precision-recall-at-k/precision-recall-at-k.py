import numpy as np
def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    recommended=np.asarray(recommended)
    relevant=np.asarray(relevant)
    result=recommended[:k]
    common = np.intersect1d(result, relevant)
    return [len(common)/k,len(common)/len(relevant)]
    