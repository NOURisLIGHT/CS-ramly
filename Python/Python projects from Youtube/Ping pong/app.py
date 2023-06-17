#importing turtle module
import turtle

wind = turtle.Screen() #initialize the screen
wind.title("Ping Pong By Codezilla")  #making the title of the screen
wind.bgcolor("black")  #background color
wind.setup(width=800, height=600)  #length and width
wind.tracer(0)  #stops the window from updating automatically


#madrab1
madrab1 = turtle.Turtle() #initialize tutrle object(shape)
madrab1.speed(0) #set the speed of the animation
madrab1.shape("square") #set the shape of the object
madrab1.color("blue")  # set the color of the shape
madrab1.penup() #stops the object from drawing lines
madrab1.goto(-350, 0) #set the starting position of the object
madrab1.shapesize(stretch_wid=5, stretch_len=1) #stretches the size of the shape

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red") 
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball  = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white") 
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5 # Each time the ball change by 0.5 pixels
ball.dy = 0.5

#score
score1 = 0
score2 = 0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Plaeyr 2: 0", align="center", font=("Courier", 24, "normal"))

#movement of madrab 1 up: 
def madrab1_up():
    y = madrab1.ycor() #gets the y coordinate of madrab1
    y += 20 #increase y coordinate by 20 pixels
    madrab1.sety(y) # Set the y of madrab1 to the new y coordinate
#movement of madrab 1 down:
def madrab1_dn():
    y = madrab1.ycor()
    y -= 20  # decrease y coordinate by 2-
    madrab1.sety(y)

#movement of madrab 2 up:
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
#movement of madrab 2 down:
def madrab2_dn():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


#keyboard bindings
wind.listen() # Tells the window to expect keyboard input
wind.onkeypress(madrab1_up, "w") #move madrab1 up when pressing w
wind.onkeypress(madrab1_dn, "d") #move madrab1 donw when pressing s
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_dn, "Down")

#main game loop
while True:
    wind.update() #updates the screen everytime the loop runs

    #move the ball
    ball.setx(ball.xcor()+ ball.dx) #ball starts at 0 on x and everytime loop runs, the ball coordinate increase by 0.5 on x axis 
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 on y and everytime loop runs, the ball coordinate increase by 0.5 on y axis

    #border check
    if ball.ycor() > 290: # if ball reached top border:
        ball.sety(290) # set y coordinate = +290
        ball.dy *= -1  #reverse the direction
    
    if ball.ycor() < -290: #if ball at bottom border:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # if ball at right border:
        ball.goto(0, 0) #return ball to center
        ball.dx *= -1 #reverse direction of the ball
        score1 += 1
        score.clear()
        score.write("Player 1: {} Plaeyr 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Plaeyr 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
         
    #collision of madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    