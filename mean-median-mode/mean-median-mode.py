from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
 mean=float(sum(x)/len(x))
 c=Counter(x)
 mode=float(c.most_common(1)[0][0])
 x.sort()
 if len(x)%2==0:
    median=float((x[(len(x)//2)-1]+x[(len(x)//2)])/2)
 else:
     median=float(x[((len(x)+1)//2)-1])



 return{
     "mean":mean , "median":median ,"mode": mode
 }