import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


fig=plt.figure(figsize=(10,10))
ax = plt.axes()


plt.xlim(0,10)
plt.ylim(0,10)

def animfunc(i):
    plt.scatter(random.randrange(0,10),random.randrange(0,10))


animation = FuncAnimation(fig, animfunc, interval=100, save_count=5)

plt.show()