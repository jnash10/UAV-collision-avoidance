import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Drone():
    def __init__(self,start,goal):
        self.start= start
        self.goal = goal
        self.roundabout = None
        self.currentx = [start[0]]
        self.currenty = [start[1]]
        self.name = ""

    def coords(self):
        return (self.currentx[-1],self.currenty[-1])


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
    y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d

    return (x,y)

class Goal():
    def __init__(self,coords):
        self.coords=coords

d1 = Drone((0,0),Goal((10,10)))
d2 = Drone((10,0),Goal((0,10)))

x = [d1.coords()[0], d2.coords()[0], intersection(d1,d2)[0],d1.goal.coords[0],d2.goal.coords[0]]
y = [d1.coords()[1], d2.coords()[1], intersection(d1,d2)[1],d1.goal.coords[1],d2.goal.coords[1]]
plt.xlim(-1,11)
plt.ylim(-1,11)
plt.scatter(x,y)
plt.show()
