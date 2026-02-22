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

#run test block if file is run manually
if __name__ == "__main__":
    print(caesar_encrypt("Hello", 3, True))
    print(caesar_decrypt("Khoor", 3, True))
    print(affine_encrypt("HELLO", 5, 8, True))
    print(affine_decrypt("RCLLA", 5, 8, True))

    