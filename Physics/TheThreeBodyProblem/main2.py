import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy 
import random

#First we try 2D motion in matplotlib plotting

initial_cordinates = []
while True:
    x=random.randint(-1000,1000)
    y=random.randint(-1000,1000)
    c = [x,y]
    if c not in initial_cordinates:
        initial_cordinates.append(c)
        if len(initial_cordinates)==2:
            break
        else:
            continue     
    else:
        pass


print(initial_cordinates)

xaxis = [initial_cordinates[0][0],initial_cordinates[1][0]]
yaxis = [initial_cordinates[0][1],initial_cordinates[1][1]]

fig= plt.subplot()
body = mpatches.Circle([1,1],2)
fig.add_artist(body)
plt.show()
