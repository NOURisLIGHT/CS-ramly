word = input("Enter a word: ")

reverse = word[::-1]

if (reverse == word):
    print("The word is Palindrome")
else:
    print("Not Palindrome")