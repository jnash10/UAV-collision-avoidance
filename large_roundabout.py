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

def intersection(d1,d2):
    x1 = d1.coords()[0]
    y1 = d1.coords()[1]

    x2 = d1.goal.coords[0]
    y2 = d1.goal.coords[1]

    x3 = d2.coords()[0]
    y3 = d2.coords()[1]

    x4 = d2.goal.coords[0]
    y4 = d2.goal.coords[1]


    d = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    x = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))/d
    y = ((x1*y2-y1*x2)-(y1-y2)*(x3*y4-y3*x4))/d

    return (x,y)
    

###### some basic initialisation values
detection_radius = 4
collision_radius=0.2
avoid_radius=0.5
goal_strength=0.08
roundabout_strength=0.5
roundabout_radius=0.2
theta_thereshold = np.pi*5/180


class Drone():
    def __init__(self,start,goal,name):
        self.start= start
        self.goal=goal
        self.roundabout=None
        self.name=name
        self.currentx=[start[0]]
        self.currenty=[start[1]]
    
    def coords(self):
        return (self.currentx[-1],self.currenty[-1])

    #return difference between angle formed by drone, goal and start, goal
    def theta(self):
        theta_start = np.arctan2(self.goal.coords[1]-self.start[1],self.goal.coords[0]-self.start[0])
        theta_current = np.arctan2(self.goal.coords[1]-self.coords()[1],self.goal.coords[0]-self.coords()[0])
        return np.abs(theta_current-theta_start)
    
    def del_goal(self):
        current = self.coords()
        theta = np.arctan2((self.goal.coords[1]-current[1]),(self.goal.coords[0]-current[0]))
        return (goal_strength*np.cos(theta),goal_strength*np.sin(theta))

    def del_roundabout(self):
        current = self.coords()
        roundabout=self.roundabout

        theta = np.arctan2((roundabout.coords[1]-current[1]),(roundabout.coords[0]-current[0])) - np.pi/2
        d = dist(current,roundabout.coords)
        
        if d < roundabout.radius:
            return(-np.sign(np.cos(theta))*np.inf,-np.sign(np.sin(theta))*np.inf)
        elif roundabout.radius <= d <= roundabout.radius + roundabout.influence:
            return (-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.cos(theta),-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.sin(theta))
        
        if roundabout.radius <= d <= roundabout.radius + roundabout.influence:
            return (-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.cos(theta),-roundabout.strength*(roundabout.influence+roundabout.radius-d)*np.sin(theta))    
        else:
            return (0,0)


    def update_pos(self):
        delg = self.del_goal()
        delr = (0,0) 
        if self.roundabout:
            delr = self.del_roundabout()
        current = self.coords()
        self.currentx.append(current[0]+delg[0]+delr[0])
        self.currenty.append(current[1]+delg[1]+delr[1])

    def check_collision(self,drones):
        if not self.roundabout:
            for drone in drones:
                if drone.name != self.name:
                    if dist(drone.coords(),self.coords()) < detection_radius:
                        if drone.roundabout:
                            self.roundabout=Roundabout(drone.roundabout.coords)
                            self.roundabout.max = drone.roundabout.max + avoid_radius
                            self.roundabout.influence = self.roundabout.max
                            break
                    if dist(drone.coords(),self.coords()) < 1*avoid_radius:
                        new_roundabout = Roundabout(((self.coords()[0]+drone.coords()[0])/2,(self.coords()[1]+drone.coords()[1])/2))
                        self.roundabout = new_roundabout
                        drone.roundabout = new_roundabout
                        break
        '''if self.roundabout:
            if dist(self.coords(),self.roundabout.coords)>self.roundabout.influence:
                self.roundabout = None'''
        for drone in drones:
            if drone.name != self.name:
                if dist(drone.coords(),self.coords()) < collision_radius:
                    print("collision ",drone.name,self.name,drone.roundabout.influence, self.roundabout.influence)


    
class Goal():
    def __init__(self,coords):
        self.coords=coords

class Roundabout():
    def __init__(self,coords):
        self.coords = coords
        self.radius = roundabout_radius
        self.influence = avoid_radius
        self.strength = roundabout_strength
        self.max = avoid_radius


goals = [Goal((0,10)),Goal((10,0)), Goal((10,10)),Goal((10,5)),Goal((0,5))]
#goals = [Goal((0,10)),Goal((10,0))]
#goals = [Goal((10,0)),Goal((10,5))]


#drones = [Drone((0,9),goals[1],"2"),Drone((0,0),goals[2],"3"),Drone((-1,5),goals[3],"4"),Drone((11,5),goals[4],"5")]
drones = [Drone((5,0),goals[0],"1"),Drone((0,9),goals[1],"2"),Drone((0,0),goals[2],"3"),Drone((-1,5),goals[3],"4"),Drone((11,5),goals[4],"5")]
#drones = [Drone((0,9),goals[1],"2"),Drone((-1,5),goals[3],"4")]

def func_anim(i):
    plt.xlim(-1,11)
    plt.ylim(-1,11)

    for goal in goals:
        ax.add_patch(plt.Circle(goal.coords,0.3, fc='blue'))

    clist = ['red','green','blue','yellow','pink']
    for i in range(len(drones)):
        drone = drones[i]
        drone.check_collision(drones)
        drone.update_pos()
        if drone.roundabout:
            #print(drone.name,drone.roundabout.coords,drone.roundabout.influence)
            ax.add_patch(plt.Circle(drone.roundabout.coords,drone.roundabout.influence, fill=False))

    
        plt.scatter(drone.currentx[-1],drone.currenty[-1],c=clist[i])

animation = FuncAnimation(fig, func_anim, interval=300)

plt.show()
print("finished")

