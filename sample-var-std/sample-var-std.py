import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x=np.array(x)
    mean=np.mean(x)
    resi=0
    for i in range(len(x)):
        resi+=(mean-x[i])**2

    
    sample_var=resi/(len(x)-1)
    return{'variance':float(sample_var),'standard_deviation':float(np.sqrt(sample_var))}