import para
import numpy as np
def cal_gravity():
    for i in range(len(para.position)):
        para.acceleration[i]=[0,-9.81,0]