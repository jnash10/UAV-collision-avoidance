import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from objects import Drone, Goal, colours
from functions import dist, intersection



fig = plt.figure(figsize=(12,12))
ax = plt.axes()



goals = [Goal((10,10)),Goal((0,10)), Goal((0,5))]


drones = [Drone((0,0),goals[0]),Drone((10,0),goals[1]),Drone((10,1),goals[2])]


 

plt.xlim(-1,11)
plt.ylim(-1,11)
def anim_func(i):
    for drone in drones:


        plt.scatter(drone.currentx,drone.currenty, c = colours[drones.index(drone)])
        drone.update_pos()

animation = FuncAnimation(fig, anim_func, interval = 100)

plt.show()