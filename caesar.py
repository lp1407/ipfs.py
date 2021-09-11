def encrypt(key, plaintext):
    ciphertext=""

    for i in range(len(plaintext)):
        saveLetter = plaintext[i]
        ciphertext += chr((ord(saveLetter) + key - 65) % 26 + 65)
        #ord takes one string character and returns its ASCII integer
        #chr takes an integer between 0 and 225 and returns its corresponding ASCII
        print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        wordHolder = ciphertext[i]
        plaintext += chr((ord(wordHolder) - key - 65) % 26 +65)

    return plaintext
