num = int(input("Enter a number: "))
fact = 1
while num != 0:
    fact = fact * num
    num -= 1
print("the factorial of the number is ", fact)
