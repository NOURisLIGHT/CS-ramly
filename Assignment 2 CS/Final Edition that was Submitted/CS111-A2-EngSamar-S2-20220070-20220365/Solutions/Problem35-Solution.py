string = input("Enter any type of text: ")
i = int(input("Enter a number less than the length of the text: "))
string = string.replace(string[i], "")
print(string)
