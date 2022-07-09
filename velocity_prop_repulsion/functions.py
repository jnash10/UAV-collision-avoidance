import numpy as np
import random

def dist(drone1,drone2):
    return np.linalg.norm(drone1.pos-drone2.pos)

def heading(drone1,drone2):
    return np.arctan2(drone1.pos[1]-drone2.pos[1],drone1.pos[0]-drone2.pos[0])

def strength(vel):
    return vel*2


def create_colours(n):
    colours = []
    random.seed(7)
    for i in range(n):
        colours.append((random.random(),random.random(),random.random()))
    return colours