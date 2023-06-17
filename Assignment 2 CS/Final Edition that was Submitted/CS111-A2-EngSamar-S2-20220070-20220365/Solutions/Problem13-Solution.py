num = int(input("Enter a number: "))
if num > 1:
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    print("The positive factors of the number are ", factors)
elif num == 1 or -1:
    print("the positive factor of the number is ", num)
elif num == 0:
    print("The factors of zero are all the numbers")
else:
    num = -num
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    print("The positive factors of the number are ", factors)
