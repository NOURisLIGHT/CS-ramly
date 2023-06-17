# Open the file to save the data in, in write mode
f1 = open(input("Enter the file you want to save the output in: "), "w")

# Open the input file you want to get the data from
with open(input("Enter the file to take the data from: "), "r") as myfile:
	data = myfile.read()


data_1 = data[::-1]
f1.write(data_1)

f1.close()
