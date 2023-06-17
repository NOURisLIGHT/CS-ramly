#ask the user if he wants it easy, medium or hard, choose the domain on that
#if easy, domain from 0 to 10, if medium, domain from -10 to 100, if hard, domain from -100 to 500
#choose random number from a domain that the user inputs
#create clue1: the number is +ve or -ve or non of them
#create clue2: the number is divisible by 4 or not
#create clue3: the number is even or odd
#create clue4: how many digits in the number
#If the user couldn't guess right after the five clues, he has lost

import random

def clue1(num):
    if num > 0:
        print("The number is +ve")
    else:
        print("The number is not +ve")

def clue2(num):
    if num % 4 == 0:
        print("The number is divisible by 4")
    else:
        print("The number is not divisible by 4")

def clue3(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def clue4(num):
    count = 0
    while num != 0:
        num = num//10
        count += 1
    print(f"The numbar consits of {count} digits")




while (True):

    difficulty = input("Choose the difficulty, do you want it easy, medium or hard? ").lower()
    if difficulty == "easy":
       
        domainL = 1   # [0, 10]
        domainH = 9
        print("Your domain starts from {} till {}".format(domainL, domainH))    #Tell the user his domain
        numbers = []
        for i in range(domainL, domainH, 1):
            numbers.append(i)           #make a list contains all the numbers from the domain
        num = random.choice(numbers)    #choose random number

        ###########################################################################
        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue2(num)

        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue3(num)

        if user_input != num:
            print(f"You lost, the number was {num}")
            break
        

    elif difficulty == "medium":

        domainL = -10  #[-10, 100]
        domainH = 100
        print("Your domain starts from {} till {}".format(domainL, domainH))
        numbers = []
        for i in range(-10, 100, 1):
            numbers.append(i)
        num = random.choice(numbers)

        ###############################################################3
        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n: ").lower()
        if ask_for_clue == "y":
            clue1(num)
        
        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n: ").lower()
        if ask_for_clue == "y":
            clue2(num)

        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n: ").lower()
        if ask_for_clue == "y":
            clue3(num)

        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n: ").lower()
        if ask_for_clue == "y":
            clue4(num)
        user_input = int(input("Try to guess the number: "))

        if user_input != num:
            print(f"You lost, the number was {num}")
            break


    elif difficulty == "hard":

        domainL = -100 #[-100, 500]
        domainH = 500
        print("Your domain starts from {} till {}".format(domainL, domainH))
        numbers = []
        for i in range(-100, 500, 1):
            numbers.append(i)
        num = random.choice(numbers)
        ######################################################################
        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue1(num)
        
        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue2(num)

        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue3(num)

        user_input = int(input("Try to guess the number: "))
        if user_input == num:
            print("Wow! You won!")
            break
        else:
            print("Wrong guess!")
        ask_for_clue = input("Do you want a clue? Type y or n").lower()
        if ask_for_clue == "y":
            clue4(num)

        if user_input != num:
            print(f"You lost, the number was {num}")
            break

    else:
        print("Invalid input!")
        break
    

