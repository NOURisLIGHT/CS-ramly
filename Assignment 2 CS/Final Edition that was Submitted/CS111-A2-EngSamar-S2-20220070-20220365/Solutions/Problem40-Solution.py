num = int(input("Enter the max num: "))
a = 0
b = 1

if (num == 1):
    print(a)
elif (num == 2):
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, num, 1):
        c = a + b
        a = b
        b = c
        print(c)