string = input("Enter a string: ")
letter = 0
digit = 0

for i in range(len(string)):
    
    # .isdigit() checks if a thing is a digit or not
    if (string[i].isdigit()):
        digit += 1
    # .isalpha() checks if a thing is a letter or not
    elif (string[i].isalpha()):
        letter += 1
        
print("The digits are", digit)
print("The letters are", letter)
        
        
    