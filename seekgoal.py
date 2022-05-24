from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np


x = [0]
y = [1]
fig = plt.figure(figsize=(12,12))


goal = (10,10)
start = (0,0)
alpha = 0.5
r=0.2
s = 4

def dist(x0,y0):
    return np.sqrt((goal[0]-x0)**2 + (goal[1]-y0)**2)



def delta(current,r,s):
    d = dist(current[0],current[1])
    theta = np.arctan((goal[1]-current[1])/(goal[0]-current[0]))

    if d<r:
        return (0,0)
    elif r<=d<=s+r:
        return (alpha*(d-r)*np.cos(theta),alpha*(d-r)*np.sin(theta))
    else:
        return (alpha*s*np.cos(theta),alpha*s*np.sin(theta))

current = start


def anim_func(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)
    plt.scatter(goal[0], goal[1], s = 100,c='blue')
    current = (x[-1],y[-1])
    delta_val = delta(current, r, s)
    current =  (current[0]+delta_val[0],current[1]+delta_val[1]) 

    x.append(current[0])
    y.append(current[1])

    
    plt.scatter(x,y)
animation = FuncAnimation(fig, anim_func, interval=500)

plt.show()


