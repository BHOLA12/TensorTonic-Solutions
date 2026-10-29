import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    mean=p
    vari=p*(1-p)
    pmf=[]
    for i in range(len(x)):
        if x[i]==1:
            pmf.append(p)
        else:
            pmf.append(1-p)
    pmf=np.array(pmf)
    return {'pmf':pmf,'mean':float(mean),'variance':float(vari)}
    