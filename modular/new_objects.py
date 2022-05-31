import numpy as np
from functions import dist, intersection

check_dist = 0.5


class Drone():
    def __init__(self,start,goal,name=""):
        self.start= start
        self.goal = goal
        self.roundabout = None
        self.roundaboutd = np.Inf
        self.currentx = start[0]
        self.currenty = start[1]
        self.name = name



    def del_goal(self): #return delta values to add that represent pull of goal
        
        theta = np.arctan2((self.goal.coords[1]-self.currenty),(self.goal.coords[0]-self.currentx))
        if dist(self.coords(),self.goal.coords) > self.goal.radius:
            return (self.goal.strength*np.cos(theta),self.goal.strength*np.sin(theta))
        else:
            return (0,0)

    def del_roundabout(self): #return delta values to add that represent pull of roundabout
        if self.roundabout:#only perform claculatiosn if drone has a roundabout
            current = self.coords()
            roundabout = self.roundabout

            theta = np.arctan2(roundabout.coords[1]-current[1],roundabout.coords[0]-current[0]) + np.pi/2
            d = dist(self.coords(),roundabout.coords)

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

        for drone in drones: #for every drone
            d = dist(self.coords(), drone.coords()) #calculate the distance
            if dist(self.coords(),drone.coords()) < check_dist and drone != self: #if the distance is less than the threshold distance
                #check if the other drone has a roundabout and if it is closer than the current roundabout distance, if yes, join it
                if drone.roundabout and dist(drone.roundabout.coords,self.coords()) < dist(intersection(self,drone),self.coords()):
                    self.roundabout = drone.roundabout
                else: #form a new roundabout
                    #new_roundabout = Roundabout(((self.coords()[0]+drone.coords()[0])/2,(self.coords()[1]+drone.coords()[1])/2))
                    new_roundabout = Roundabout(intersection(self,drone))
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
        self.strength = 0.05
        self.radius = 0.001 #if you're closer than this that means youve reached the goal

class Roundabout(): #roundabout class
    def __init__(self,coords):
        self.coords = coords
        self.strength = 0.8
        self.radius = 0.25


colours = ['green','red','blue','pink','grey','orange','magenta']




