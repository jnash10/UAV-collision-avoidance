import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from random import randrange
from functions import create_colours
from objects import *
from steps import step


fig = plt.figure(figsize=(10,10))
ax = plt.axes()
plt.xlim(0,1500)
plt.ylim(0,1500)

drones = []

n = int(input("please enter how many drones you want (integer): "))

random.seed(15)

for i in range(n):
    drones.append(Drone((randrange(0,1500),randrange(0,1500)),(randrange(0,1500),randrange(0,1500)),randrange(2,8)))
drones = [Drone((100,0),(100,1000),8),Drone((0,100),(1000,100),3),Drone((0,200),(1000,200),3),Drone((0,300),(1000,300),2),Drone((0,400),(1000,400),2)]
n=len(drones)
colours = create_colours(n)

for k in range(n):
    ax.add_patch(plt.Circle(drones[k].goal,radius=10,color='blue'))



def anim_func(i):
    for j in range(n):
        drone = drones[j]

        plt.scatter(drone.pos[0],drone.pos[1],s=5,c=colours[j])

        step(drone,drones)

        

animation = FuncAnimation(fig, anim_func, interval=50)

plt.show()
