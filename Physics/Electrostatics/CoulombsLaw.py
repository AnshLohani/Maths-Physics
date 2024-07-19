import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools as iter

q=1
Q=1

def yax(r):
    func = (9*(10**9)*Q*q)/(r**2)
    return func
    

def animate(i):
    r = next(n)
    xaxis.append(r)
    yaxis.append(yax(r))
    plt.cla()
    plt.xlabel("Distace")
    plt.ylabel("Force")
    plt.plot(xaxis,yaxis,color = 'red')
    pass


try:
    ani = FuncAnimation(plt.gcf(), animate, interval = 1)

    xaxis=[]
    yaxis=[]
    n = iter.count(1)

    plt.tight_layout()
    plt.show()
except:
    print("Some Error...")
    