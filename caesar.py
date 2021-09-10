def encrypt(key, plainte):
    ciphertext = ""
    for i in range(len(plaintext)):
        wordHolder = plaintext[i]

        ciphertext += chr((ord(wordHolder)+key-65) % 26+65)
       
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    return plaintext
