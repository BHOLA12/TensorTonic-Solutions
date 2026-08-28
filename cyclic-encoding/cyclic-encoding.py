import math

def cyclic_encoding(values: list, period: float) -> list:
     result=[]
     for i in range(len(values)):
        angle=(2*(math.pi)*values[i])/period
        result.append([math.sin(angle),math.cos(angle)])
     return result
     