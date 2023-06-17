start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
nums = []
for i in range(start, end + 1):
    if i % 9 == 0 and i % 4 != 0:
        nums.append(i)
print("The nums that are divisible by 9 and not by 4 are", nums)
