import para,math
def cal_collision():
    m=1000
    num=0
    for i in range(len(para.position)):
        if para.type[i]!=0:
                continue
        for j in para.neightable[i]:
            if i==j:
                continue
            rIJ=para.position[j]-para.position[i]
            distanceIJ=math.sqrt(rIJ[0]*rIJ[0]+rIJ[1]*rIJ[1]+rIJ[2]*rIJ[2])
            if distanceIJ>para.initial_distance*0.5:
                continue
            uIJ=para.velocity[j]-para.position[i]
            forceDT=(uIJ[0]*rIJ[0]+uIJ[1]*rIJ[1]+uIJ[2]*rIJ[2])/distanceIJ
            if forceDT>0:
                forceDT*=(1.0+0.2)*m/2.0
                velocity_i=(forceDT/m)*rIJ/distanceIJ
                para.position[i]+=(velocity_i-para.velocity[i])*para.dt
                para.velocity[i]=velocity_i
                num+=1
    print(num)


