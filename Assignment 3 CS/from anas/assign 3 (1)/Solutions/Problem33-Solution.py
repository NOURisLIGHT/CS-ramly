def sort(lst):
    x = 0
    for i in range(len(lst) - 1):
        x = 1
        if lst[i] >= lst[i + 1]:
            x = 0
            break
    if x == 0:
        for i in range(len(lst) - 1):
            x = -1
            if lst[i] <= lst[i + 1]:
                x = 0
                break
    return x


list = [1, 2, 3, 4]
print(sort(list))
