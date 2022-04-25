import para,weight
import numpy as np
import math
def cal_pressure():
    c2=10*10
    rho=1000
    n0=para.nzero
    for i in range(len(para.position)):
        if para.type[i]==3 or para.type[i]==-1 :
            para.pressure[i]=0.0
        else:
            ni=para.numberdensity[i]
            if ni>para.nzero:
                para.pressure[i]=(c2*rho*(ni-para.nzero))/para.nzero
            else:
                para.pressure[i]=0.0

def cal_pressuregradient():
    a=para.numberofdimensions/para.nzero
    for i in range(len(para.position)):
        gradientI=np.array([0.0,0.0,0.0])
        if para.type[i]!=0:
            continue
        for j in para.neightable[i]:
            if i==j:
                continue
            if para.type[j]==3 or para.type[j]==-1 :
                continue
            rIJ=para.position[j]-para.position[i]
            distanceIJ=math.sqrt(rIJ[0]*rIJ[0]+rIJ[1]*rIJ[1]+rIJ[2]*rIJ[2])
            if distanceIJ<para.initial_distance*para.radius_ratio:
                w=weight.weight(distanceIJ)
                pij=(para.pressure[i]+para.pressure[j])/(distanceIJ*distanceIJ)
                gradientI+=rIJ*pij*w
        gradientI=a*gradientI
        para.acceleration[i]+=(-1.0)*gradientI/1000

        


