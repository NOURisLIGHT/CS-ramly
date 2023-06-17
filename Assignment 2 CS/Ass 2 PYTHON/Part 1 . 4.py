
number = int(input("Enter a number: "))

factorial = 1

if (number < 0): 
    print("Can't compute the factorial of -ve numbers")
elif(number < 2):
    print("{}! = {}".format(number, factorial))
else: 
    for num in range(number, 0, -1):
        factorial = factorial * num
        
    print("{}! = {}".format(number, factorial))