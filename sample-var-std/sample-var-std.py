import numpy as np

def sample_var_std(x: list) -> dict:
    x=np.array(x)
    
    mean= np.mean(x)
    s=0.0
    for i in range(len(x)):
        s=s+float((((x[i]-mean)**2)/(len(x)-1)))

    vari=float(np.sqrt(s))


    return {"variance":s ,"standard_deviation":vari}
    