print("enter three numbers below")
x = int(input())
y = int(input())
z = int(input())

if x - y == z:
    print(str(x) + " - " + str(y) + " = " + str(z))
elif x + y == z:
    print(str(x) + " + " + str(y) + " = " + str(z))
elif x * y == z:
    print(str(x) + " * " + str(y) + " = " + str(z))
elif x / y == z:
    print(str(x) + " / " + str(y) + " = " + str(z))
elif x ** y == z:
    print(str(x) + " ** " + str(y) + " = " + str(z))
else:
    print("There is no any operations between these numbers")