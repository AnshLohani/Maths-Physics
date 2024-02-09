import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def random_num():
    a = random.randrange(-1,2,2)
    return a

#x-axis --> value of the slot
#y-axis --> number of balls that droped in that slot
#n = int(input("Enter number of pins: "))
#numb = int(input("Enter number of times to execute: "))

n=10

xaxis = list()
for x in range(-n-5,n+6):
    xaxis.append(x)

xy_dict = dict()
for i in xaxis:
    xy_dict[i] = 0

yaxis = list()

def yaxisdef(n):
    global xy_dict,yaxis

    y = 0
    for i in range(n+1):
            y = y + random_num()
    xy_dict[y]+=1

    temp = xy_dict.values()
    return temp


def animate(i):
    yaxis = yaxisdef(n)

    plt.cla()
    plt.bar(xaxis,yaxis,color = 'black',width=2)
    pass

ani = FuncAnimation(plt.gcf(), animate, interval = 1)

plt.tight_layout()
plt.show()