import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    mse=0;
    for i  in range(len(y_pred)):
     mse+=(y_pred[i]-y_true[i])**2


    return mse/len(y_pred)
    