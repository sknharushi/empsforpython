import para,math,weight
import numpy as np

def cal_viscosity():
    kinematic_viscosity=float(1.0E-6)
    coefficient=float(kinematic_viscosity*2*para.numberofdimensions/(para.lambda0*para.nzero))
    for i in range(len(para.position)):
        viscosity_term=np.array([0.0,0.0,0.0])
        if para.type[i]!=0:
            continue
        for j in para.neightable[i]:
            if i==j:
                continue
            rIJ=para.position[j]-para.position[i]
            distanceIJ=math.sqrt(rIJ[0]*rIJ[0]+rIJ[1]*rIJ[1]+rIJ[2]*rIJ[2])
            if distanceIJ<para.initial_distance*para.radius_ratio:
                w=weight.weight(distanceIJ)
                uIJ=para.velocity[j]-para.position[i]
                viscosity_term+=uIJ*w
        viscosity_term*=coefficient
        para.acceleration[i]+=viscosity_term