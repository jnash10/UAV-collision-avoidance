import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import pi
from dubins import dubins
from objects import *
from ZEM import *
from functions import *

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
plt.xlim(-1000,1500)
plt.ylim(-1000,1500)

drone = Drone((0,0),(1000,1000),pi/4)
drone2 = Drone((0,1000),(1000,0),-pi/4)

def anim_func(i):
    plt.scatter(drone.xcoord,drone.ycoord,s=5)
    plt.scatter(drone2.xcoord,drone2.ycoord,s=5)
    ax.add_patch(plt.Circle(drone.goal,radius=5,color='blue'))
    ax.add_patch(plt.Circle(drone2.goal,radius=5,color='blue'))
    dubins(drone)
    dubins(drone2)
    print(t_go(drone,drone2),zem(drone,drone2),dist((drone.xcoord,drone.ycoord),(drone2.xcoord,drone2.ycoord)))
    
    




animation = FuncAnimation(fig, anim_func, interval=1000)

plt.show()
