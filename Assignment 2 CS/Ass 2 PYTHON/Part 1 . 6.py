arr = [1, 3, 5, 6, 8, 8, 3, 2, 6, 8]
i = 0

if (len(arr) % 2 == 0):
    while i in range(len(arr)):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
    print(arr)

else:
    print("Invalid entry")
