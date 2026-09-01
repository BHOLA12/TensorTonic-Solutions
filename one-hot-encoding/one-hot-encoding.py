import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    arr=np.array(y)
    
    one_hot=[]
    if num_classes is None:
       num_classes=np.max(arr)+1 
    one_hot = np.zeros((len(y), num_classes), dtype=float)
    for i  in range(len(y)):
        one_hot[i][y[i]]=1
    return one_hot

    
    