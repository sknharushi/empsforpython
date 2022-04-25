import para,weight
import math
import numpy as np
def calnZeroandlambda():
    if para.numberofdimensions==2:
        Z_start=0
        Z_end=1
    else:
        Z_start=-4
        Z_end=5
    xi=0
    yi=0
    zi=0
    for i in range(-4,5):
        for j in range(-4,5):
            for k in range(Z_start,Z_end):
                if i==0 and j==0 and k==0:
                    continue
                xj=para.initial_distance*i
                yj=para.initial_distance*j
                zj=para.initial_distance*k
                distance_square=(xj-xi)*(xj-xi)+(yj-yi)*(yj-yi)+(zj-zi)*(zj-zi)
                distance=math.sqrt(distance_square)
                para.nzero+=weight.weight(distance)
                para.lambda0+=distance_square*weight.weight(distance)
    para.lambda0=para.lambda0/para.nzero
    print('nzero',para.nzero)
    print('lambda',para.lambda0)




    x=1
def init_main():
    para.acceleration=np.zeros((len(para.position),3),dtype='float64')
    calnZeroandlambda()