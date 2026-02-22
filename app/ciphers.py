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
                shifted = (ord(char)-offset+shift)%26
                result += chr(shifted+offset)
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

#run test block if file is run manually
if __name__ == "__main__":
    print(caesar_encrypt("Hello", 3, True))
    print(caesar_decrypt("Khoor", 3, True))

