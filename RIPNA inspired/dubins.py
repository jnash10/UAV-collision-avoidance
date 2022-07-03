from objects import *
from numpy import arctan2, cos, sin
from parameters import *
from functions import *

def check_heading(drone): #returns true if drone heading towards goal
    #print(drone.heading - arctan2(drone.goal[1]-drone.ycoord,drone.goal[0]-drone.xcoord),drone.heading,arctan2(drone.goal[1]-drone.ycoord,drone.goal[0]-drone.xcoord))
    if abs(arctan2(drone.goal[1] - drone.ycoord,drone.goal[0] - drone.xcoord) - drone.heading) < heading_threshold:
        return True
    else:
        return False


def get_cp_cm(drone): #return c+, c-
    c1 = (drone.xcoord  - r_min*sin(drone.heading), drone.ycoord + r_min*cos(drone.heading))
    c2 = (drone.xcoord  + r_min*sin(drone.heading), drone.ycoord - r_min*cos(drone.heading))
    if dist(c1, drone.goal) < dist(c2, drone.goal):
        return c1, c2
    else:
        return c2, c1


def check_cp(drone,cp):
    if dist(cp, drone.goal) < r_min:
        return True
    else:
        return False

def clip_angle(angle):
    if -pi<angle<=pi:
        return angle
    elif angle>pi:
        return angle - 2*pi
    elif angle < -pi:
        return angle + 2*pi

def dubins(drone):
    drone.heading = clip_angle(drone.heading)

    if dist((drone.xcoord,drone.ycoord),drone.goal) >= reached_distance: #only do if destination not yet reached


        #if uav heading to goal:
        if check_heading(drone):
            #keep going
            #print("heading correct")
            pass
        #else:
        else:
            #print("correcting heading")
            #get c+, c-
            
            cp, cm = get_cp_cm(drone)
            
            #if c+ encircles goal:
            if check_cp(drone, cp):
                #go along C-
                #print("going to c-")
                if drone.heading - arctan2(drone.goal[1]-drone.ycoord,drone.goal[0]-drone.xcoord) > 0:
                    drone.heading = drone.heading + speed*render_time/r_min
                else:
                    drone.heading = drone.heading - speed*render_time/r_min
            else:
                #go along c+
                #print("going to c+")
                if drone.heading - arctan2(drone.goal[1]-drone.ycoord,drone.goal[0]-drone.xcoord) > 0:
                    drone.heading = drone.heading - speed*render_time/r_min
                else:
                    drone.heading = drone.heading + speed*render_time/r_min

        
        

    
        drone.xcoord = drone.xcoord + speed*cos(drone.heading)*render_time
        drone.ycoord = drone.ycoord + speed*sin(drone.heading)*render_time




