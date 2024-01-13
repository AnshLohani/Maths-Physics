import math as m
import matplotlib.pyplot as plt

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

def seconds(sec):

    seconds_vals = list()
    n = 2
    s = sec
    while True:
        t = best_time(n)
        if t <= s:
            seconds_vals.append(t)
            n+=1
        else:
            break

    for x in range(2,s+1):
        print(f"{x} came ",seconds_vals.count(x), " times")    

def graph(num):
    x = num
    xaxis = list()
    yaxis = list()

    for i in range(2,x+1):
        xaxis.append(i)
        yaxis.append(best_time(i))
    
    plt.plot(xaxis,yaxis)
    plt.show()


print(best_time(17))