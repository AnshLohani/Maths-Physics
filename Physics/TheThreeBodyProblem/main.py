import turtle
import random 



#Defining Initial Locations 
def vectorpos(x):
    '''
    x --> list()
    x = [x1,y1] --> 2D cordinates of body "a"
        
    returns a vector 'va' } nested list
    Format: x = [ [ax,i] [ay,j] ]
    ''' 
    vx = [[x[0],"i"],[x[1],"j"]]
    return vx
        
    
def vel_a():
        ...

def vel_b():
        ...
def vel_c():
        ...


#Making a screen!
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1080, height=720)






#initial cordinates for the 3 bodies
initial_cordinates = []
while True:
    x=random.randint(-screen.window_width() // 2 + 20, screen.window_width() // 2 - 20)
    y=random.randint(-screen.window_height() // 2 + 20, screen.window_height() // 2 - 20)
    c = [x,y]
    if c not in initial_cordinates:
        initial_cordinates.append(c)
        if len(initial_cordinates)==3:
            break
        else:
            continue     
    else:
        pass



'''
simulation = {t1:[x,y],...}
#t1 = [mass="10"]
'''


t1=turtle.Turtle(shape="circle")
t2=turtle.Turtle(shape="circle")
t3=turtle.Turtle(shape="circle")
bodies = [t1,t2,t3]
for i in bodies:
    i.shapesize(10)
    i.color("white")


simulation = dict()
simulation[t1]=[initial_cordinates[0][0],initial_cordinates[0][1]]
simulation[t2]=[initial_cordinates[1][0],initial_cordinates[1][1]]
simulation[t3]=[initial_cordinates[2][0],initial_cordinates[2][1]]


print(simulation)



while True:
    la = vectorpos([t1.xcor(),t1.ycor()])
    lb = vectorpos([t2.xcor(),t2.ycor()])
    lc = vectorpos([t3.xcor(),t3.ycor()])

    screen.update()






screen.exitonclick()
