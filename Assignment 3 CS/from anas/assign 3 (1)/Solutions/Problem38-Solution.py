file = open("doesn't matter.txt",  "r")
data = file.read()

lines = len(data.split("\n"))   #-->  Each new line will be considered as split, and it will count each split
words = len(data.split())       #--> Each space will be considered as split, which will count the number of words
chars = len(data)               #--> It returns by default the whole number of charachters in the file

print("LINES = ", lines)
print("WORDS = ", words)
print("CHARS = ", chars)