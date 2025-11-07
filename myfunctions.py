import turtle

bob=turtle.Turtle()


def square (size):
    bob.forward(150)
    bob.left(90)
    bob.forward(150)
    bob.left(90)

def triangle (size):
    bob.forward(150)
    bob.left(120)
    bob.forward(150)
    bob.left(120)
    bob.forward(150)


def polygon (size, side, c):
    bob.color(c)
    angle=360 / side
    for times in range(size):
        bob.forward (size)
        bob.left (angle)

def comet(size,angle,amt):
    for times in range(amt):
        bob.width(times)
        bob.forward(size)
        bob.left(angle)

def jump (x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def stair(distance, amount, c, w):
    bob.color(c)
    bob.width(w)
    for times in range (amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)

def drawsquare( sizeS, sizeC ):
    for times in range (4):
        bob.forward(sizeS)
        bob.right(90)
        bob.circle(sizeC)

turtle.colormode(255)

def flower (size):
   

   bob.width(25)
   bob.color("green")
   bob.forward(500)
   for times in range(6):
       polygon(3,100,"red")
       bob.left(45)
       bob.begin_fill()
       bob.circle(75)
       bob.circle(50)
       bob.end_fill()


    
    

       
       
       
       
       
