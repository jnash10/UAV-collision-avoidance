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
    def __init__(self, start, goal, roundabout= None, name=""):
        self.goal = goal
        self.start = start
        self.currentx=[start[0]]
        self.currenty=[start[1]]
        self.roundabout = None
        self.name=name
        
    
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
    
    def update_avoid(self, roundabout):
        current = (self.currentx[-1],self.currenty[-1])
        #print(current)

        theta = np.arctan2((roundabout.coords[1]-current[1]),(roundabout.coords[0]-current[0])) - np.pi/2
        #theta = np.arctan2((roundabout.coords[1]-current[1]),(roundabout.coords[0]-current[0]))
        d = dist(current,roundabout.coords)

        if d < roundabout.radius:
            return(-np.sign(np.cos(theta))*np.inf,-np.sign(np.sin(theta))*np.inf)
        elif roundabout.radius <= d <= roundabout.radius + roundabout.influence:
            return (-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.cos(theta),-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.sin(theta))

        else:
            return (0,0)
    
    def update_delta(self, roundabout):
        delr = (0,0)
        if roundabout:
            delr = self.update_avoid(roundabout)
        

        delg = self.update_goal()

        current = (self.currentx[-1],self.currenty[-1])

        self.currentx.append(current[0] + delr[0] + delg[0])
        self.currenty.append(current[1] + delr[1] + delg[1])
    
    def coords(self):
        return (self.currentx[-1],self.currenty[-1])

    def theta(self):
        theta_start = np.arctan2(self.goal.coords[1]-self.start[1],self.goal.coords[0]-self.start[0])
        theta_current = np.arctan2(self.goal.coords[1]-self.coords()[1],self.goal.coords[0]-self.coords()[0])
        return np.abs(theta_current-theta_start)




def update_roundabout(drones):

    for i in range(len(drones)):
        drone = drones[i]
        #if you're already in a roundabout:
        if drone.roundabout:
            #if theta_goal is small:
            if drone.theta() < 10*np.pi/180 :

                #exit from roundabout( make roundabout= None)
                drone.roundabout = None
            
        #elif someone comes within d of you and you're not in a roundabout:
        if drone.roundabout == None:
            for j in range(len(drones)):
                if j != i:
                    compare = drones[j]
                    if dist(compare.coords(),drone.coords()) < 1:

                        #if they have a roundabout, join it
                        
                        if compare.roundabout:
                            drone.roundabout = compare.roundabout
                        

                        #if they don't have a roundabout, create one between you 2
                        else:
                            drone.roundabout = Goal(((drone.coords()[0]+compare.coords()[0])/2,(drone.coords()[1]+compare.coords()[1])/2),0.1,0.3,1)
                            compare.roundabout = Goal(((drone.coords()[0]+compare.coords()[0])/2,(drone.coords()[1]+compare.coords()[1])/2),0.1,0.3,1)
  


            
            






    
    
        
class Goal(): #the goal class to define goals
    def __init__(self,coords,strength,radius,influence):
        self.coords = coords
        self.strength=strength
        self.radius=radius
        self.influence = influence

        


goals = [Goal((0,10),0.01,0.3,4),Goal((10,0),0.02,0.3,2), Goal((10,10),0.01,0.3,4),Goal((10,5),0.01,0.3,4),Goal((0,5),0.01,0.3,4)]
#goals = [Goal((0,10),0.01,0.3,4),Goal((10,0),0.04,0.3,2)]



drones = [Drone((9,0),goals[0],name="1"),Drone((0,9),goals[1],name="2"),Drone((0,0),goals[2],name="3"),Drone((-1,5),goals[3],name="4"),Drone((11,5),goals[4],name="5")]
#drones = [Drone((9,0),goals[0]),Drone((0,9),goals[1])]



def anim_func(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)

    

    for goal in goals:
        ax.add_patch(plt.Circle(goal.coords,goal.radius, fc='blue'))
    
    


    update_roundabout(drones)

    clist = ['red','green','blue','yellow','pink']
    for i in range(len(drones)):
        drone = drones[i]
        drone.update_delta(drone.roundabout)
    
        plt.scatter(drone.currentx[-1],drone.currenty[-1],c=clist[i])
        #ax.add_patch(plt.Circle((drone.currentx[-1],drone.currenty[-1]), 0.5, fill=False))
        #print(drone.theta())

    



animation = FuncAnimation(fig, anim_func, interval=85)

plt.show()

    