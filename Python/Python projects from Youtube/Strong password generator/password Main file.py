import string   #import string module
import random

# make lists for (lower/upper/digits/punctuation)
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


#take number of charachters from the user
charachters_number = input("Enter a number of charachters at least 6: ")
while True:
    try:
        #make sure the input is integer number
        charachters_number = int(charachters_number)
        #make sure number of charachters is 6 or more
        if charachters_number < 6:
            print("You need at least 6 charachters")
            charachters_number = input("Enter a number of charachters at least 6: ")
        else:
            break
    except:
        print("Please enter a number")
        charachters_number = input("Enter a number for the password: ")


#shuffle lists by importing "random" module then calling the function shuffle from it
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#calculate 25% of lower case and upper case, then  30% numbers, then 20% punctuations
part1 = round(charachters_number * (25/100)) #lower case will take 25%, upper case will take 25%
part2 = round(charachters_number * (30/100)) # digits will take 30%
part3 = round(charachters_number * (20/100)) # punctuations will take 20%


#create password 50% letters and 30% digits and 20% punctuation
password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])

for i in range(part3):
    password.append(s4[i])

#shuffle the password then join it
random.shuffle(password)
password = "".join(password[0:])

print(password)