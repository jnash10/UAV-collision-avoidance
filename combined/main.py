import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from move import *

from objects import *
from functions import *
import random
from random import randrange

import pandas as pd



fig = plt.figure(figsize=(10,10))
ax = plt.axes()
plt.xlim(-1000,1500)
plt.ylim(-1000,1500)

random.seed(5)


#drones = [Drone((0,1000),(1000,1000)),Drone((1000,1000),(0,1000)), Drone((500,500),(500,1500)), Drone((500,1500),(500,-500))]
drones = [Drone((0,0),(1000,50)),Drone((0,300),(1000,50))]



# drones = []

# n = int(input("please enter how many drones you want (integer): "))

# for i in range(n):
#     drones.append(Drone((randrange(-1000,1500),randrange(-1000,1500)),(randrange(-1000,1500),randrange(-1000,1500))))



def create_colours(n):
    colours = []
    random.seed(7)
    for i in range(n):
        colours.append((random.random(),random.random(),random.random()))
    return colours

colours = create_colours(len(drones))
table = init_table(drones)

def anim_func(i):
    for j in range(len(drones)):
        drone = drones[j]
        print(drone.pos)
        plt.scatter(drone.pos[0],drone.pos[1],s=5,c=colours[j])
        simple_move(drone)
        check_dist(drone,drones)
        
        ax.add_patch(plt.Circle(drone.goal,radius=5,color='blue'))


        for k in range(j):
            neighbour = drones[k]
            d = dist(drone,neighbour)
            #print(d,table[j][k],d>table[j][k])

            if d < table[j][k]:
                table[j][k] = d
        
        
        
    
animation = FuncAnimation(fig, anim_func, interval=10)

plt.show()

print(table)

data = pd.DataFrame(table)

pd.DataFrame.to_csv(data,'data.csv')