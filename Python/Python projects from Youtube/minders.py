# Importing modules
import turtle
import random


#-----------------------
# Setting up the turtles
#-----------------------
p1 = turtle.Turtle()
p1.color("green")
p1.shape("turtle")
p1.penup()
p1.goto(-200, 100)

p2 = p1.clone()
p2.color("blue")
p2.penup()
p2.goto(-200, -100)



#-------------------------
# Setting up the endlines
#-------------------------
p1.goto(300, 60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200, 100)

p2.goto(300, -140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200, -100)


# Setting up the die that we will take randomly from
die = [1, 2, 3, 4, 5, 6]


# Developing the game
for i in range(20):
    
    if p1.pos() >= (300, 100):
        print("P1 is the winner")
        break

    elif p2.pos() >= (300, -140):
        print("P2 is the winner")
        break

    else:
        p1_turn = input("P1 press enter to roll")
        die_try = random.choice(die)
        print("The die outcome is ", die_try)
        p1.fd(20 * die_try)

        p2_turn = input("P2 press enter to roll")
        die_try = random.choice(die)
        print("The die outcome is ", die_try)
        p2.fd(20 * die_try)
