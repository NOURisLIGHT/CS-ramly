word = input("Enter a word: ")
list_word = list(word)
len = len(word)
for i in range(0, len):
    list_word[i] = word[len-1-i]
rev_word = ''.join(list_word)
if word == rev_word:
    print("this word is palindrome")
print(rev_word)
