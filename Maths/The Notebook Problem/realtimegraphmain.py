import math as m
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

def time(x,n):
    ftime = m.ceil(m.log(x,2)) + m.ceil(n/x)
    return ftime

def best_time(n):
    bt = n
    for x in range(2,n+1):
        if time(x,n) <= bt:
            bt = time(x,n)
        else:
            continue
    
    return bt

def animate(i):
    t = next(num)
    xaxis.append(t)
    yaxis.append(best_time(t))

    plt.cla()
    plt.plot(xaxis,yaxis)

xaxis = []
yaxis = []
num = count(2)

ani = FuncAnimation(plt.gcf(), animate, interval = 1)

plt.tight_layout()
plt.show()