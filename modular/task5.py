import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from objects_3 import *
from functions import *
import random
from random import randrange
from time import time

import pandas as pd

random.seed(6)

fig = plt.figure(figsize=(10,10))
ax = plt.axes()


#collision menas distance less than
collision_dist=0.5
#goals = [Goal((10,10)),Goal((0,10)), Goal((0,5)),Goal((5,10)),Goal((1,10)),Goal((0.5,10))]


#drones = [Drone((0,0),(10,10),"green"),Drone((10,0),(0.5,10)),Drone((10,1),(0,10)),Drone((5,0),(0,5)),Drone((9,0),(1,10))]
#drones = [Drone((10,0),goals[5],"green"),Drone((10,1),goals[1],"red"),Drone((9,0),goals[4],"blue")]

drones = []

n = int(input("please enter how many drones you want (integer): "))

for i in range(n):
    drones.append(Drone((randrange(0,101),randrange(0,101)),(randrange(0,101),randrange(0,101))))

#drones = [Drone((0,0),(100,100)),Drone((100,0),(0,100)),Drone((0,100),(100,0)),Drone((100,100),(0,0))]

plt.xlim(0,101)
plt.ylim(0,101)

for drone in drones:
    plt.scatter(drone.goal.coords[0],drone.goal.coords[1],s=30,c='blue')

table = init_table(drones)
colours = create_colours(len(drones))
def anim_func(i):
    for j in range(len(drones)):
        drone = drones[j]


        plt.scatter(drone.currentx,drone.currenty,s=5,c=colours[j])
        #check for exiting roundabout
        drone.check_exit()
        #chek for new roundabout
        drone.check_roundabout(drones)
        #now update to position
        drone.update_pos()
        #printing the roundabouts formed
        if drone.roundabout:
            ax.add_patch(plt.Circle((drone.roundabout.coords),radius=drone.roundabout.radius,fill=False,alpha=0.5))
            plt.scatter(drone.roundabout.coords[0],drone.roundabout.coords[1],s=10,c='black')
        if drone.name == "green":
            if drone.roundabout:
                print("yes")
            else:
                print("no")

        #store distances
        for k in range(j):
            neighbour = drones[k]
            d = dist(drone.coords(),neighbour.coords())
            #print(d,table[j][k],d>table[j][k])

            if d < table[j][k]:
                table[j][k] = d
            if d< collision_dist:
                plt.scatter(drone.roundabout.coords[0],drone.roundabout.coords[1],s=15,c='red')

            



            



animation = FuncAnimation(fig, anim_func, interval = 1)

plt.show()


print(table)

data = pd.DataFrame(table)

pd.DataFrame.to_csv(data,'data.csv')