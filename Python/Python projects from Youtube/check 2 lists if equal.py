# Program to check if two lists are equal even if there are duplicates

list1 = list(input("Enter the elements of your first list separeted by space: ").split())
list2 = list(input("Enter the elements of your second list separeted by space: ").split())

flag = True
for i in list1:
    if i in list2:
        continue
    else:
        flag = False
        break

for i in list2:
    if i in list1:
        continue
    else:
        flag = False
        break



if flag == True:
    print("The lists are the same")
else: 
    print("The lists are different")
        
