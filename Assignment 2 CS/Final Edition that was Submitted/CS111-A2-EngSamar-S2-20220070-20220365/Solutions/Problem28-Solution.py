num = input("Enter a number: ")
result = 0

# Calc. the sum of cubes of the number's digits
for i in range(len(num)):
    s = int(num[i])
    result += s ** 3

# Comparing the number with the cubes of its digits
if int(num) == result:
    print("The given number is Armstrong")
else:
    print("The given number is not Armstrong")

# 0, 1, 153, 370, 371 are armstrong nums
