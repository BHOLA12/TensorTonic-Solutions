import math
from math import comb

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    resi= comb(n,k)*((p)**k)*(1-p)**(n-k)
    result=0;
    for i in  range(k+1):
      result+=comb(n,i)*((p)**i)*(1-p)**(n-i)
    return {"pmf":float(resi),"cdf":float(result)}
    