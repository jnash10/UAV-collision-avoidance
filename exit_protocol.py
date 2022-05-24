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
    def __init__(self, start, goal, roundabouts = []):
        self.goal = goal
        self.start = start
        self.currentx=[start[0]]
        self.currenty=[start[1]]
        self.roundabouts = []
        
    
    def update_goal(self):
        current = (self.currentx[-1],self.currenty[-1])
        #print(current)

        theta = np.arctan2((self.goal.coords[1]-current[1]),(self.goal.coords[0]-current[0]))
        d = dist(current,self.goal.coords)
        #print(d)

        if d < self.goal.radius:
            return (0,0)

        #elif self.goal.radius < d < self.goal.radius + self.goal.influence:

            #return (self.goal.strength*(d-self.goal.radius)*np.cos(theta),self.goal.strength*(d-self.goal.radius)*np.sin(theta))

        else:
            return (self.goal.strength*self.goal.influence*np.cos(theta),self.goal.strength*self.goal.influence*np.sin(theta))
    

    
    def update_delta(self, roundabouts):
        delr = (0,0)

        delg = self.update_goal()

        current = (self.currentx[-1],self.currenty[-1])

        self.currentx.append(current[0] + delr[0] + delg[0])
        self.currenty.append(current[1] + delr[1] + delg[1])
    
    def coords(self):
        return (self.currentx[-1],self.currenty[-1])

   
        
class Goal(): #the goal class to define goals
    def __init__(self,coords,strength,radius,influence):
        self.coords = coords
        self.strength=strength
        self.radius=radius
        self.influence = influence

        


#goals = [Goal((0,10),0.01,0.3,4),Goal((10,0),0.02,0.3,2), Goal((10,10),0.01,0.3,4),Goal((10,5),0.01,0.3,4),Goal((0,5),0.01,0.3,4)]
goals = [Goal((0,10),0.01,0.3,4),Goal((10,0),0.04,0.3,2)]



#drones = [Drone((9,0),goals[0]),Drone((0,9),goals[1]),Drone((0,0),goals[2]),Drone((-1,5),goals[3]),Drone((11,5),goals[4])]
drones = [Drone((9,0),goals[0]),Drone((0,9),goals[1])]



def anim_func(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)

    

    for goal in goals:
        ax.add_patch(plt.Circle(goal.coords,goal.radius, fc='blue'))
    

    clist = ['red','green','blue','yellow','pink']
    for i in range(len(drones)):
        drone = drones[i]
        drone.update_delta(drone.roundabouts)
    
        plt.scatter(drone.currentx[-1],drone.currenty[-1],c=clist[i])
        #ax.add_patch(plt.Circle((drone.currentx[-1],drone.currenty[-1]), 0.5, fill=False))
        #print(drone.currentx)

    



animation = FuncAnimation(fig, anim_func, interval=85)

plt.show()