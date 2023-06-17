def equal_lists(lst1, lst2):
    for i in lst1:
        for l in lst2:
            x = False
            if i == l:
                x = True
                break
        if not x:
            return False
            break
        else:
            return True


list1 = [2, 5, 3, 4, 1]
list2 = [1, 2, 3, 4, 5]

print(equal_lists(list1, list2))
