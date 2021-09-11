def encrypt(key, plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        wordHolder = plaintext[i]

        ciphertext += chr((ord(wordHolder)+key-65) % 26+65)
       
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        wordHolder = ciphertext[i]
        plaintext += chr((ord(wordHolder) - 65) % 26 +65)
        plaintext = plaintext [::-1]
        print(plaintext)
    return plaintext
