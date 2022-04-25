import numpy as np
import para
import math,weight
def cal_density():
    for i in range(len(para.position)):
        para.numberdensity[i]=0
        for j in para.neightable[i]:
            if i==j:
                continue
            rIJ=para.position[j]-para.position[i]
            distanceIJ=math.sqrt(rIJ[0]*rIJ[0]+rIJ[1]*rIJ[1]+rIJ[2]*rIJ[2])
            w=weight.weight(distanceIJ)
            para.numberdensity[i]+=w