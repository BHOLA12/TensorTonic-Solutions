import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x=np.array(x,dtype=float)
    expected_val=0.0
    for i in range(len(x)):
        expected_val+=p[i]*x[i]
    return expected_val