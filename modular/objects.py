import numpy as np
from functions import dist

check_dist = 0.5


class Drone():
    def __init__(self,start,goal):
        self.start= start
        self.goal = goal
        self.roundabout = None
        self.currentx = start[0]
        self.currenty = start[1]
        self.name = ""



    def del_goal(self): #return delta values to add that represent pull of goal
        
        theta = np.arctan2((self.goal.coords[1]-self.currenty),(self.goal.coords[0]-self.currentx))
        return (self.goal.strength*np.cos(theta),self.goal.strength*np.sin(theta))

    def del_roundabout(self): #return delta values to add that represent pull of roundabout
        if self.roundabout:#only perform claculatiosn if drone has a roundabout
            current = self.coords()
            roundabout = self.roundabout

            theta = np.arctan2(roundabout.coords[1]-current[1],roundabout[0]-current[0]) + np.pi/2
            d = dist(self.coords,roundabout.coords)

            #currently im not adding a case for when d is very very small => drone is on the roundabout

            if d <= roundabout.radius:
                return (-roundabout.strength*(roundabout.radius - d)*np.cos(theta),-roundabout.strength*(roundabout.radius-d)*np.sin(theta))
            else:
                return (0,0)
        else: #if drnoe doesnt have a roundabout no changes in delta
            return (0,0)

    def update_pos(self): #adds pulls of goal and roundabout to current position
        delg = self.del_goal() #delta from goal
        delr = self.del_roundabout() #delta from roundabout
        self.currentx = self.currentx + delg[0] + delr[0] #adding both to current position
        self.currenty = self.currenty + delg[1] + delr[1]

    def coords(self): #returns coordinates of drone in (x,y)
        return (self.currentx,self.currenty)

    def theta(self): #return angle formed by drone -> roundabout -> goal
        a = dist(self.roundabout.coords,self.goal.coords)
        b = dist(self.coords(), self.roundabout.coords)
        c = dist(self.coords(), self.goal.coords)

        return np.arccos((a**2 + b**2 - c**2)/(2*a*b))

    def check_roundabout(self, drones): #compare distances with all other drones to see if need to form a roundabout
        if not self.roundabout: #only do this if you already don't have a roundabout, if you have a roundabout, continue on it
            for drone in drones:
                if dist(self.coords(),drone.coords()) < check_dist:
                    #check if the other drone has a roundabout already, if yes, join it
                    if drone.roundabout:
                        self.roundabout = drone.roundabout
                    else: #form a new roundabout
                        new_roundabout = Roundabout(((self.coords()[0]+drone.coords()[0])/2,(self.coords()[1]+drone.coords()[1])/2))
                        self.roundabout = new_roundabout
                        drone.roundabout = new_roundabout

    def check_exit(self): #checks if theta(defined above) is les sthan 90 degrees and exits the roundabout if it is
        if self.roundabout:
            angle = self.theta()
            if angle <= np.pi/2:
                self.roundabout = None

class Goal(): #goal class
    def __init__(self,coords):
        self.coords=coords
        self.strength = 0.5

class Roundabout(): #roundabout class
    def __init__(self,coords):
        self.coords = coords
        self.strength = 0.8
        self.radius = 0.5


colours = ['green','red','blue','pink','grey','orange','magenta']




