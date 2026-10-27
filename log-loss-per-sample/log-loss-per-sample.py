import math
import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    new_per = np.clip(y_pred, eps, 1 - eps)
    

   
    loos=-1*(y_true*np.log(new_per)+(1-y_true)*np.log(1-new_per))
    return loos.tolist()