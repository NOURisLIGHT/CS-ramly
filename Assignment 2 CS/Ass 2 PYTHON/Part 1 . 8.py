lst = []
length = int(input("Enter the length of the list: "))

# inputing the maximum of a list
n = int(input("Enter the max number of the list: "))

# filling the list
for i in range (length - 1):
    num = int(input("Enter a number to put in the list: "))
    lst.append(num)

# inserting the max number(n) at the end of the list
lst.insert(length, n)
print(lst)

# entering an index then deleting it
p = int(input("Now enter the index you want to delete: "))
lst.pop(p)
print(lst)
print("Here it is! xD")

