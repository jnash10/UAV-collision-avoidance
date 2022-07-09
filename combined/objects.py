from numpy import arctan2
import numpy as np

class Drone():
    def __init__(self,start,goal):
        self.start = np.array(start)
        self.goal = np.array(goal)
        self.engaged = False
        self.heading = arctan2(goal[1]-start[1],goal[0]-start[0])
        self.pos = self.start

    def correct_heading(self):
        self.heading = arctan2(self.goal[1]-self.pos[1],self.goal[0]-self.pos[0])


class Roundabout():
    def __init__(self,pos):
        self.pos= pos



