import numpy as np
import para
from scipy.spatial import cKDTree

#K-D木による近傍粒子探索
def set_table():
    points=para.position
    targets=para.position
    kd_tree = cKDTree(points)
    para.neightable=kd_tree.query_ball_point(targets,para.initial_distance*para.radius_ratio)