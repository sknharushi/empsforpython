# Written by Sekine Harufumi
import para,files,init,neigh,gravity,viscosity,pressure,collision,move,density
import numpy as np
from scipy.spatial import cKDTree
import time
def main():
    files.read_gridfile('input.grid')
    #files.read_datafile()
    init.init_main()
    istep=0
    files.make_outputfile(0)
    file_num=1
    while True:
        if para.time>2:
            break
        neigh.set_table()

        gravity.cal_gravity()
        viscosity.cal_viscosity()
        move.move()
        neigh.set_table()
        collision.cal_collision()
        neigh.set_table()
        density.cal_density()
        pressure.cal_pressure()
        pressure.cal_pressuregradient()
        move.move2()

        para.time+=para.dt
        print('time')
        print(para.time)
        if istep%50==0:
            files.make_outputfile(file_num)
            file_num+=1
        istep+=1
if __name__ == "__main__":
    main()