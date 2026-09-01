import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
     X=np.array(X,dtype=float)
     mini=np.min(X,axis=axis,keepdims=True)
     maxi=np.max(X,axis=axis,keepdims=True)
     range_ = maxi - mini
     
     

     result = np.zeros_like(X)

     np.divide(X - mini, range_, out=result, where=range_ > eps)

     return result
    
    