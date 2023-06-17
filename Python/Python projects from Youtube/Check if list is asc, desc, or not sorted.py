lst = list(input("Enter your list: ").split())

countasc = 0
countdsc = 0
flag = True
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        countasc += 1
    elif lst[i] > lst[i+1]:
        countdsc += 1
    else:
        flag = False

if countasc == (len(lst) - 1):
    print(1)
elif countdsc == (len(lst) - 1):
    print(-1)
else:
    print(0)
