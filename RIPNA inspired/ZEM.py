from numpy import dot, sqrt, cos, sin
from parameters import *
from objects import *
import numpy as np


def t_go(drone1,drone2): #return time of closest approach
    p1p2 = (drone1.xcoord-drone2.xcoord,drone1.ycoord-drone2.ycoord)
    d1d2 = (cos(drone1.heading)-cos(drone2.heading),sin(drone1.heading) - sin(drone2.heading))
    tgo = dot(p1p2,d1d2)/dot(d1d2,d1d2)
    tgo = -tgo/(speed*render_time)
    
    return tgo

    


def zem(drone1,drone2):
    tgo = t_go(drone1,drone2)
    p1p2 = (drone1.xcoord-drone2.xcoord,drone1.ycoord-drone2.ycoord)
    d1d2 = (cos(drone1.heading)-cos(drone2.heading),sin(drone1.heading) - sin(drone2.heading))
    #print(p1p2,d1d2)
    return sqrt(dot(p1p2,p1p2) + 2*np.array(dot(p1p2,d1d2))*speed*render_time*tgo + dot(d1d2,d1d2)*(speed*render_time*tgo)**2)



