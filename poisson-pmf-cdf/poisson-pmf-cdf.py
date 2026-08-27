import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
   pmf=(((math.e)**-lam)*(lam**k))/math.factorial(k) 
   cdf=0.0
   for i in range(k+1):
       cdf+=(((math.e)**-lam)*(lam**i))/math.factorial(i) 
   return {"pmf":float(pmf),"cdf":float(cdf)}