import para
def move():
    for i in range(len(para.position)):
        if para.type[i]!=0:
            continue
        para.velocity[i]+=para.acceleration[i]*para.dt
        para.position[i]+=para.velocity[i]*para.dt
        para.acceleration[i]=0
def move2():
    for i in range(len(para.position)):
        if para.type[i]!=0:
            continue
        para.velocity[i]+=para.acceleration[i]*para.dt
        para.position[i]+=para.acceleration[i]*para.dt*para.dt
        para.acceleration[i]=0