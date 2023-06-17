encrypt = {
    "a" : "d",
    "b" : "e",
    "c" : "f",
    "d" : "g",
    "e" : "h",
    "f" : "i"
}
output = ""
option = input("Enter wether you want to encrypt or decrypt: ")
if option == "encrypt":
    word = input("Enter the word you want to encrypt: ")
    for i in word:
        for key, value in encrypt.items():
            if i == key:
                j = value
                output += j
    print(output)
        
    
    
elif option == "decrypt":
    word = input("Enter word to decrypt: ")
    for i in word:
        for key, value in encrypt.items():
            if i == value:
                j = key
                output += j
    print(output)
    
    
    
    
    