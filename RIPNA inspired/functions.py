from numpy import sqrt

def dist(coord1, coord2):
    return sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)