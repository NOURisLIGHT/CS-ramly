num = input("Enter a number: ")
summ = 0

for i in range(0, len(num), 1):
    s = int(num[i])
    summ += s
print(summ)