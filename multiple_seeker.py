from re import A
from turtle import distance
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import random
import numpy as np



fig = plt.figure(figsize=(12,12))
ax = plt.axes()

#function to calculate euclidean distance
def dist(start,end):
    return np.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)

#defining a drone object. it will have a goal which it will continuously seek
#each drone will also have its delta derived from its own goal
#each drone will also have a starting point : tuple
class Drone():
    def __init__(self, start, goal):
        self.goal = goal
        self.start = start
        self.currentx=[start[0]]
        self.currenty=[start[1]]
    
    def update_delta(self):
        current = (self.currentx[-1],self.currenty[-1])
        #print(current)

        theta = np.arctan2((self.goal.coords[1]-current[1]),(self.goal.coords[0]-current[0]))
        d = dist(current,self.goal.coords)
        #print(d)

        if d < self.goal.radius:
            self.currentx.append(current[0]+0)
            self.currenty.append(current[1]+0)
            #return (0,0)

        elif self.goal.radius < d < self.goal.radius + self.goal.influence:
            
            self.currentx.append(current[0]+self.goal.strength*(d-self.goal.radius)*np.cos(theta))
            self.currenty.append(current[1]+self.goal.strength*(d-self.goal.radius)*np.sin(theta))
            #return ((self.goal.strength*(d-self.goal.radius)*np.cos(theta)),(self.goal.strength*(d-self.goal.radius)*np.sin(theta)))

        else:
            self.currentx.append(current[0]+self.goal.strength*self.goal.influence*np.cos(theta))
            self.currenty.append(current[1]+self.goal.strength*self.goal.influence*np.sin(theta))
            #return (self.goal.strength*self.goal.influence*np.cos(theta),self.goal.strength*self.goal.influence*np.sin(theta))

    
    
        
class Goal(): #the goal class to define goals
    def __init__(self,coords,strength,radius,influence):
        self.coords = coords
        self.strength=strength
        self.radius=radius
        self.influence = influence




goals = [Goal((10,10),0.1,0.3,4),Goal((7,10),0.2,0.3,2)]



drones = [Drone((1,2),goals[0]),Drone((3,1),goals[1])]



def anim_func(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)

    

    for goal in goals:
        ax.add_patch(plt.Circle(goal.coords,goal.radius, fc='blue'))

    for drone in drones:
        drone.update_delta()
        
    for drone in drones:
        plt.scatter(drone.currentx,drone.currenty)
        #print(drone.currentx)

    



animation = FuncAnimation(fig, anim_func, interval=150)

plt.show()

    