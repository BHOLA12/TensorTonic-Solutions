import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_norm2=np.linalg.norm(a,ord=2)
    b_norm2=np.linalg.norm(b,ord=2)
    if a_norm2==0 or b_norm2==0:
        return 0.0

    return float(np.dot(a,b)/(a_norm2*b_norm2))
    