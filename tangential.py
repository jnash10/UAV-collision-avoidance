from turtle import distance
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import random
import numpy as np



x = [1]
y = [0]
fig = plt.figure(figsize=(12,12))
ax = plt.axes()

x_del = []
y_del = []

goal = (10,10)
alpha=0.1
rg=0.3
sg=4

avoid = (4,3)
beta=0.3
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

@np.vectorize
def delta_copy(x,y):
    return delta((x,y))
xq,yq= np.meshgrid(np.arange(-1,11,0.2),np.arange(-1,11,0.2))
u,v = delta_copy(xq,yq)

ax.quiver(xq,yq,u,v)

def anim_func(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)

    plt.scatter(goal[0],goal[1],s=100,c='blue')
    #cg=plt.Circle((goal[0],goal[1]),sg,fill=False)
    cg1=plt.Circle((goal[0],goal[1]),rg,fc='blue')

    plt.scatter(avoid[0],avoid[1],s=50,c='red')
    #ca=plt.Circle((avoid[0],avoid[1]),sa,fill=False)
    ca1=plt.Circle((avoid[0],avoid[1]),ra,fc='red')

    current = (x[-1],y[-1])

    delta_val = delta(current)
    current =  (current[0]+delta_val[0],current[1]+delta_val[1]) 
    
    x.append(current[0])
    y.append(current[1])

  

    

    #ax.add_patch(ca)
    #ax.add_patch(cg)
    ax.add_patch(ca1)
    ax.add_patch(cg1)
    plt.scatter(x,y)


animation = FuncAnimation(fig, anim_func, interval=150)




plt.show()
    



