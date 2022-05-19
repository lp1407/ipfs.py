def encrypt(key,plaintext):
     ciphertext=""
    #YOUR CODE HERE
    for i in range(len(plaintext)) :
        char = plaintext[i]
        ciphertext += chr((ord(char) + key - 65) % 26 + 65)
    #print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    #print(ciphertext + ":")
    plaintext=""
    #YOUR CODE HERE
    for i in range(len(ciphertext)) :
        char = ciphertext[i]
        plaintext += chr((ord(char) - key - 65) % 26 + 65)
    #print(plaintext)
    return plaintext
