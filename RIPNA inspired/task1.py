import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import pi
from dubins import dubins
from objects import *
from ZEM import *
from functions import *
from mod_RIPNA import ripna

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
plt.xlim(-1000,1500)
plt.ylim(-1000,1500)



drones = [Drone((0,1000),(1000,1000),0),Drone((1000,1000),(0,1000),pi)]

def anim_func(i):
    for drone in drones:
        plt.scatter(drone.xcoord,drone.ycoord,s=5)
        
        ax.add_patch(plt.Circle(drone.goal,radius=5,color='blue'))
        
        
        ripna(drone,drones)
    
animation = FuncAnimation(fig, anim_func, interval=100)

plt.show()
