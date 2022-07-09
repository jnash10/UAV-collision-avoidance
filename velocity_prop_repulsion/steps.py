import numpy as np
from functions import *
from parameters import *

def goal_steps(drone):
    heading = np.arctan2(drone.goal[1]-drone.pos[1],drone.goal[0]-drone.pos[0])

    return drone.vel * np.array((np.cos(heading),np.sin(heading)))


def repulsion_step(drone,drones):
    step = np.array((0,0))
    for other in drones:
        step_ = np.array((0,0))
        if other != drone:
            if dist(other,drone)<sensor_range:
                theta = np.arctan2(other.pos[1]-drone.pos[1],other.pos[0]-drone.pos[0])
                step_ = -constant*strength(other.ideal_vel)*np.array(np.cos(theta),np.sin(theta))/dist(other,drone)
        step = step + step_

    return step





def step(drone,drones):
    step = goal_steps(drone) + repulsion_step(drone,drones)
    print(goal_steps(drone))




    drone.pos = drone.pos + step
    



        
