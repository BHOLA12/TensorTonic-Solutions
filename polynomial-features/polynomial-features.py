def polynomial_features(values: list, degree: int) -> list:
    if len(values)<1 or degree<0:
        return []
    result=[]
    for i in  range(len(values)):
        res=[]
        for j in range(degree+1):
            res.append(values[i]**j)
        
        result.append(res) 
    return result