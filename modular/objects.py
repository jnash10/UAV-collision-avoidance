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

class Goal():
    def __init__(self,coords):
        self.coords=coords


