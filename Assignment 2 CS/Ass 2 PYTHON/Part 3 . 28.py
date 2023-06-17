num = input("Enter a number: ")
result = 0

# Calc. the sum of cubes of the num's digits
for i in range(0, len(num), 1):
    s = int(num[i])
    result += s * s * s
    
# Comparing the number with the cubes of its digits
if (int(num) == result):
    print("The given number is an Armstrong")
else:
    print("Try Again")
    
    
# 0, 1, 153, 370, 371 are armstrong nums 