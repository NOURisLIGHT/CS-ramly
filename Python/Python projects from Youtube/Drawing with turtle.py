import turtle

s = turtle.Turtle()
s.speed(10)
s.color("black", "yellow")
s.begin_fill()
for i in range(100):
    s.forward(200)
    s.left(170)
s.end_fill()
    
turtle.done()