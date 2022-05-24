from turtle import distance
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import random
import numpy as np




fig = plt.figure(figsize=(12,12))
ax = plt.axes()

x_del = []
y_del = []

goal = (10,10)
alpha=0.1
rg=0.2
sg=2

avoid = (4,3)
beta=0.5
ra=0.2
sa=2


def dist(start,end):
    return np.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)

def delta_attract(current,goal):
    theta = np.arctan2((goal[1]-current[1]),(goal[0]-current[0]))
    d = dist(current,goal)
    if d<rg:
        return (0,0)
    elif rg<=d<=sg+rg:
        return (alpha*(d-rg)*np.cos(theta),alpha*(d-rg)*np.sin(theta))
    else:
        return (alpha*sg*np.cos(theta),alpha*sg*np.sin(theta))

def delta_revolve(current,avoid):
    theta = np.arctan2((avoid[1]-current[1]),(avoid[0]-current[0])) + np.pi/2
    d = dist(current,avoid)

    if d<ra:
        return(-np.sign(np.cos(theta))*np.inf,-np.sign(np.sin(theta))*np.inf)
    elif ra<=d<=ra+sa:
        return (-beta*(sa+ra-d)*np.cos(theta),-beta*(sa+ra-d)*np.sin(theta))
    else:
        return (0,0)

def delta(current):
    del_g = delta_attract(current,goal)
    del_a = delta_revolve(current,avoid)
    return (del_a[0]+del_g[0],del_a[1]+del_g[1])


xq,yq = np.meshgrid(np.arange(0,12,0.1),np.arange(0,12,0.1))


@np.vectorize
def delta_copy(x,y):
    return delta((x,y))

u,v = delta_copy(xq,yq)

ax.quiver(xq,yq,u,v)






plt.show()








