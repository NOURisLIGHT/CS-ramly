#import string module
#make lists for (upper/lower/digits/punctuations)
#take number of pass charachters from the user
#check if the input is number or not
#check if the number is greater than or equal to 6 or not
#shuffle lists by importing "random" module then calling the function shuffle from it
#calculate 25% of lower case and upper case, then  30% numbers, then 20% punctuations

#create password 50% letters and 30% digits and 20% punctuation
#shuffle the password then join it

import string
import random

s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

while True:
    charachters_number = input("Enter the number of charachters of your password: ")
    try:
        charachters_number = int(charachters_number)
        if charachters_number < 6:
            charachters_number = input("Enter a number greater than or equal to 6: ")
        else:
            break
    except:
        charachters_number = input("Enter a valid number of charachters for your password: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

upper_and_lower = round(charachters_number * (25/100))
digit = round(charachters_number * (30/100))
punc = round(charachters_number * (20/100))

password = []
for i in range(upper_and_lower):
    password.append(s1[i])
    password.append(s2[i])

for i in range(digit):
    password.append(s3[i])

for i in range(punc):
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])

print(password)