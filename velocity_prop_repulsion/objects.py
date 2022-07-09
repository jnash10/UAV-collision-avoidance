import numpy as np

class Drone():
    def __init__(self,start,goal,vel):
        self.pos =np.array(start)
        self.goal = np.array(goal)
        self.vel = vel
        self.ideal_vel=vel
        self.theta = 0
        


    
