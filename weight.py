import para
def weight(r):
    w=0
    if r<=0+0.0001*para.initial_distance or para.radius_ratio*para.initial_distance<r:
        w=0
    else:
        w=(para.radius_ratio*para.initial_distance/r)-1

    if w<0:
        print('error')
    return w
        
