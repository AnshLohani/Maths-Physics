from itertools import count
import math as m

n = 10

for x in range (2,n):
    f = m.log(x,2)
    t = m.ceil(f) + 1
    print(f"{x} --> ",t," seconds")

'''
Therefore the formula for finding out the best time is

t(n) = [ log2 (n) ]  where [.] is GIF function.

note: log is in base 2, its NOT n multiplied by 2 !!

'''