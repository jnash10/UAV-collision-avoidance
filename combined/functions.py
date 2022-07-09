import numpy as np
from numpy import cos, sin
from parameters import *

def dist(drone1, drone2):
    return np.linalg.norm(drone1.pos-drone2.pos)


def t_go(drone1, drone2):
    p1p2 = drone1.pos - drone2.pos
    d1d2 = np.array((cos(drone1.heading)-cos(drone2.heading),sin(drone1.heading) - sin(drone2.heading)))
    tgo = np.dot(p1p2,d1d2)/np.dot(d1d2,d1d2)
    tgo = -tgo/std_velocity

    return tgo


def zem(drone1,drone2):
    tgo = t_go(drone1,drone2)
    p1p2 = drone1.pos - drone2.pos
    d1d2 = np.array((cos(drone1.heading)-cos(drone2.heading),sin(drone1.heading) - sin(drone2.heading)))
    #print(p1p2,d1d2)
    vector = np.array((p1p2 + d1d2*std_velocity*tgo))
    return np.sqrt(np.dot(vector,vector))

def init_table(drones):
    table = np.zeros((len(drones),len(drones)))

    table = table + 1000

    return table