text = "Python"
k = 1
result = ""

# Passing over each letter in text string
for i in range(len(text)):
    
    #assigning the letter at index i to variable char
    char = text[i]
    
    #char will enter here if the letter is capital
    if char.isupper():
        
        #ord() will transfer the letter to its equivalent ASCII number
        #chr() will transfer the number to its equivalent ASCII letter
        #We wrote %26 so that if the letter is Z it will go back to A
        #So here we will transfer letter to ASCII, take 65 out of it, if it's capital, then increase ASCII number by k(which is written at L2), then convert back to equivalent letter
        # We subtract & add 65 because the minimum capital ASCII number is 65 which equals A
        s = chr(((ord(char) - 65 + k) % 26) + 65)
        result += s
    
    #It will enter here if the char is small
    else:
        # We subtract & add 97 because the min small ASCII num is 97 which equals a
        s = chr(((ord(char) - 97 + k) % 26) + 97)
        result += s
        
print(result)
    