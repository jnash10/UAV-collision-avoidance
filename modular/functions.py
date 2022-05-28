import numpy as np

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

def dist(a,b):
    d = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    return d






