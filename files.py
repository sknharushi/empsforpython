import numpy as np
import para
def read_gridfile(file_path):
    particle=[]
    text_file = open(file_path, "rt")
    tmp=0
    for line in text_file:
        if tmp>=2:
            p=np.array(list(map(float,line.split())))
            if p[0]!=-1:
                particle.append(p)
        tmp+=1
    text_file.close()
    particle=np.array(particle)
    #種類
    para.type=particle[:,0]
    #座標
    para.position=(particle[:,1:4])
    #速度
    para.velocity=particle[:,4:7]
    #圧力
    para.pressure=particle[:,7]
    #粒子数密度
    para.numberdensity=particle[:,8]
def read_datafile():
    x=1
def make_outputfile(istep):
    name='output_%04d.prof' % istep
    f = open(name, 'w')
    f.write('%f\n' % para.time)
    f.write('%d\n' % len(para.position))
    for i in range(len(para.position)):
        f.write('%d %f %f %f %f %f %f %f %f\n' %(para.type[i],para.position[i][0],para.position[i][1],para.position[i][2]\
            ,para.velocity[i][0],para.velocity[i][1],para.velocity[i][2],para.pressure[i],para.numberdensity[i]))
    f.close()
