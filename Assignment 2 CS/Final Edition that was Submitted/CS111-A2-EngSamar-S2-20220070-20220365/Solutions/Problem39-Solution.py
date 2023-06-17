low = int(input("Enter the smallest number: "))
high = int(input("Enter the highest number: "))
sum = 0
for i in range(low, high + 1):
    sum += i
print(sum)
