def encrypt(text):
    k = 1
    result = ""
    for i in range(len(text)):
        char = text[i]
    
        if char.isupper():
            s = chr(((ord(char) - 65 + k) % 26) + 65)
            result += s
        
        elif char.islower():
            s = chr(((ord(char) - 97 + k) % 26) + 97)
            result += s
    print(result)
    return result

def decrypt(text):
    k = -1
    result_decrypt = ""
    for i in range(len(text)):
        char = text[i]
    
        if char.isupper():
            s = chr(((ord(char) - 65 + k) % 26) + 65)
            result_decrypt += s
        
        elif char.islower():
            s = chr(((ord(char) - 97 + k) % 26) + 97)
            result_decrypt += s
    print(result_decrypt)
    
    
encrypt("I love Python Programming.")
decrypt("JmpwfQzuipoQsphsbnnjoh")