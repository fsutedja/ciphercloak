import math

def caesar_encrypt(text, shift, preserve_case=True):
    result = "" #initialize result

    #loop each character
    for char in text:
        if char.isalpha(): #only shift letters
            if preserve_case: #keep case
                #finds offset to convert letters to 0-25 range
                if char.isupper():
                    offset = ord('A') #ascii of 'A'
                else:
                    offset = ord('a') #ascii of 'a'
            else:
                char = char.lower()
                offset = ord('a')
            shifted = (ord(char)-offset+shift)%26
            result += chr(shifted+offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift, preserve_case=True):
    return caesar_encrypt(text, -shift, preserve_case)

def affine_encrypt(text, a, b, preserve_case=True):
    result = ""

    if math.gcd(a,26) == 1:
        for char in text:
            if char.isalpha():
                if preserve_case:
                    if char.isupper():
                        offset = ord('A') #ascii of 'A'
                    else:
                        offset = ord('a') #ascii of 'a'
                else:
                    char = char.lower()
                    offset = ord('a')
                
                p = ord(char) - offset #alphabet index of current char
                encrypted = (a*p+b)%26
                result += chr(encrypted+offset)
            else:
                result += char
        return result
    else:
        raise ValueError("Invalid key. 'a' must be relatively prime to 26.")

def affine_decrypt(text, a, b, preserve_case=True):
    result = ""

    if math.gcd(a,26) == 1:

        a_inverse = pow(a, -1, 26)
        
        for char in text:
            if char.isalpha():
                if preserve_case:
                    if char.isupper():
                        offset = ord('A') #ascii of 'A'
                    else:
                        offset = ord('a') #ascii of 'a'
                else:
                    char = char.lower()
                    offset = ord('a')
                
                p = ord(char) - offset #alphabet index of current char
                decrypted = (a_inverse*(p-b))%26
                result += chr(decrypted+offset)
            else:
                result += char
        return result
    else:
        raise ValueError("Invalid key. 'a' must be relatively prime to 26.")

def vigenere_encrypt(text, key, preserve_case=True):
    result = ""

    #key must only have letters
    key_index = 0
    clean_key = ""
    for char in key:
        if char.isalpha():
            clean_key += char.lower()
    if clean_key == "":
        raise ValueError("Key must contain at least one letter!")

    for char in text:
        if char.isalpha():
            if preserve_case:
                if char.isupper():
                    offset = ord('A') #ascii of 'A'
                else:
                    offset = ord('a') #ascii of 'a'
            else:
                char=char.lower()
                offset = ord('a')
            
            key_char = clean_key[key_index%len(clean_key)] #char that determines shift value
            shift = ord(key_char) - ord('a')

            p = ord(char) - offset
            encrypted = (p+shift)%26
            result += chr(encrypted+offset)

            key_index+=1
        else:
            result += char
    
    return result

def vigenere_decrypt(text, key, preserve_case=True):
    result = ""

    #key must only have letters
    key_index = 0
    clean_key = ""
    for char in key:
        if char.isalpha():
            clean_key += char.lower()
    if clean_key == "":
        raise ValueError("Key must contain at least one letter!")

    for char in text:
        if char.isalpha():
            if preserve_case:
                if char.isupper():
                    offset = ord('A') #ascii of 'A'
                else:
                    offset = ord('a') #ascii of 'a'
            else:
                char=char.lower()
                offset = ord('a')
            
            key_char = clean_key[key_index%len(clean_key)] #char that determines shift value
            shift = ord(key_char) - ord('a')

            p = ord(char) - offset
            decrypted = (p-shift)%26
            result += chr(decrypted+offset)

            key_index+=1
        else:
            result += char
    
    return result

#run test block if file is run manually
if __name__ == "__main__":
    print(caesar_encrypt("Hello", 3, True))
    print(caesar_decrypt("Khoor", 3, True))
    print(affine_encrypt("HELLO", 5, 8, True))
    print(affine_decrypt("RCLLA", 5, 8, True))
    print(vigenere_encrypt("ATTACKATDAWN", "LEMON", True))
    print(vigenere_decrypt("LXFOPVEFRNHR", "LEMON", True))

