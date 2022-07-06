

class Drone():
    def __init__(self,position,goal,heading):
        self.xcoord = position[0]
        self.ycoord = position[1]
        self.goal = goal
        self.heading = heading
        self.engaged = False


        
