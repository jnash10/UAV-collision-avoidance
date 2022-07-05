from ZEM import *
from parameters import *
from functions import *
from dubins import dubins


def ripna(drone,drones):
    sensed = []
    for other in drones:
        if other != drone:
            if dist((other.xcoord,other.ycoord),(drone.xcoord,drone.ycoord)) < sensor_range:
                sensed.append(other)
                print(dist((other.xcoord,other.ycoord),(drone.xcoord,drone.ycoord)))
    
    closeby = []
    timings = []
    for other in sensed:
        if t_go(other,drone) > 0 and zem(other,drone) <= near_miss :
            closeby.append(other)
            timings.append(t_go(other,drone))
    if timings:
        index = timings.index(min(timings))
        colliding_drone = closeby[index]
        #print("collision happening")
        drone.heading = drone.heading + speed*render_time/r_min
        colliding_drone.heading = colliding_drone.heading + speed*render_time/r_min
        #print(dist((drone.xcoord,drone.ycoord),(colliding_drone.xcoord,colliding_drone.ycoord)))
        
    else:
        dubins(drone)



