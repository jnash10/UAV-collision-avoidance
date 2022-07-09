import numpy as np
from functions import *
from parameters import sensor_range
def simple_move(drone):
    if not drone.engaged:

        drone.pos = drone.pos + std_velocity*np.array((np.cos(drone.heading),np.sin(drone.heading)))

        drone.correct_heading()




def check_dist(drone,drones):
    for other in drones:
        if other != drone:
            if dist(drone,other)<sensor_range:
                if t_go(drone,other)>0 and zem(drone,other)<safe_zone:
                    drone.heading = drone.heading + std_velocity/r_min
                    other.heading = other.heading + std_velocity/r_min
