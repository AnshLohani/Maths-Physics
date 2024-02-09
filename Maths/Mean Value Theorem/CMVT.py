import random
import matplotlib.pyplot as plt 


####
# n ---> no. of pens 
# x ---> no. of times to run 
####
def random_num():
    a = random.randrange(-1,2,2)
    return a



def plot_CMVT(n,x):
    templist = list()
    tempdict = dict()
    for l in range(-x,x+1):
        tempdict[l] = 0
    for j in range(x):
        z=0
        for i in range(n):
            x = random_num()
            z=z+x
        templist.append(z)
    templist.sort()
    for i in templist:
        tempdict[i] = templist.count(i)   
    xaxis = list()
    xaxis = tempdict.keys()
    yaxis = list()
    yaxis = tempdict.values()
    plt.plot(xaxis,yaxis)
    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    plt.show()


n=20
x=100
plot_CMVT(n,x)
