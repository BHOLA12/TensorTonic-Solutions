
import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    nCr = math.comb(n, k)
    
    pmf = nCr * (p**k) * ((1-p)**(n-k))
    cdf = 0.0
    for i in range(k+1):
        ncr = math.comb(n, i)
        cdf += ncr * (p**i) * ((1-p)**(n-i))
    
    return {"pmf": float(pmf), "cdf": float(cdf)}