import turtle
import random 

#Defining Initial Conditions of Bodies a, b, c.
class initial_conditions:
    #Defining Initial Locations 
    def location_a(a):
        '''
        a --> list()
        a = [x1,y1] --> 2D cordinates of body "a"
        
        returns a vector 'va' } nested list
        Format: va = [ [ax,i] [ay,j] ]
        ''' 
        va = [[a[0],"i"],[a[1],"j"]]
        return va
        

    def location_b(b):
        '''
        b --> list()
        b = [x2,y2] --> 2D cordinates of body "b"
        returns a vector 'vb' } nested list
        Format: vb = [ [bx,i] [by,j] ]
        ''' 
        vb = [[b[0],"i"],[b[1],"j"]]
        return vb

    def location_c(c):
        '''
        c --> list()
        c = [x3,y3] --> 2D cordinates of body "c"
        returns a vector 'vc' } nested list
        Format: cb = [ [cx,i] [cy,j] ]
        ''' 
        vc = [[c[0],"i"],[c[1],"j"]]
        return vc
    
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


# Body definitions (mass, radius, color)
bodies = [
    [10, 20],
    [15, 20],
    [20, 20],
]

# Create the turtles for each body
turtles = []
for body in bodies:
    t = turtle.Turtle()
    t.shape("circle")
    t.shapesize(body[1] / 10)  # Scale circle size based on radius
    t.color("white")
    turtles.append(t)

# Random starting positions (within screen boundaries)
for t in turtles:
    t.penup()
    x = random.randint(-screen.window_width() // 2 + body[1], screen.window_width() // 2 - body[1])
    y = random.randint(-screen.window_height() // 2 + body[1], screen.window_height() // 2 - body[1])
#    z = random.randint(-screen.window_height() // 2 + body[1], screen.window_height() // 2 - body[1])
    t.setx(x)
    t.sety(y)
    t.pendown()


while True:
    for t in turtles:
        # Random change in direction
        t.setheading(random.randint(0, 360))
        # Move forward based on mass (larger = slower)
        t.forward(10)

    screen.update()






screen.exitonclick()
