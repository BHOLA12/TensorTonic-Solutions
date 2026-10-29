from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x=np.array(x,  dtype=float)
    mean=np.mean(x)
    median=np.median(x)
    values, counts = np.unique(x, return_counts=True)
    print(counts)
    resi=np.argmax(counts)
    mode=values[resi]
    return {'mean':float(mean),'median':float(median),'mode':float(mode)}