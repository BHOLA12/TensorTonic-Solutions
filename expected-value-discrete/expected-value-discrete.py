import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    result=0
    for i in range(len(x)):
       result+=x[i]*p[i]
        
    return float(result)