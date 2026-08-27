import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    
    # Write code here
    result=[]
    meani=p
    var=p*(1-p)
    for i in range(len(x)):
        if x[i]==1:
            result.append(p)
        else:
            result.append(1-p)
    result=np.array(result)

    return {"pmf":result,"mean":float(meani),"variance":float(var)}
   