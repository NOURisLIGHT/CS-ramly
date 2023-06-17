read_file = open("file.txt", "r")
file = read_file.read().split()
l = len(file)
for i in range(l-1):
    temp = file[i]
    file[i] = file[l-1-i]
    file[l-1-i] = temp
print(file)
read_file.close()
