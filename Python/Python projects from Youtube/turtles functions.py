# Importing all turtle functions using astrisk
from turtle import *


# Defining a function that draws any polygon
def polygon(turtle, sides, length_of_side):
    for i in range(sides):
        turtle.forward(length_of_side)
        turtle.left(360 / sides)



# Declaring new turtle
x = Turtle()

#x.fd(distance) == x.forward(distance)
x.fd(100)

#x.lt(angle) == x.left(angle)
x.lt(90)


#drawing triangle
for i in range(3):
    x.fd(100)
    x.lt(120)


#Coloring:
x.color("red", "pink")  # Edge color, fill color
#begin_fill will fill all the drawings between it and end_fill with pink
x.begin_fill()
polygon(x, 6, 150)
x.end_fill()






#Job for this turtle is done
done()