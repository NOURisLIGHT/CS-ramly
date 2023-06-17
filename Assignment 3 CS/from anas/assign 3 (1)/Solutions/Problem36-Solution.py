f2 = open(input("Enter the file that I will paste in: "), "w")

with open(input("Enter the file that I will copy from: "), "r") as f1:
    data = f1.read()

f2.write(data)
f2.close()