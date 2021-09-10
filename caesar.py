def encrypt(key,plaintext):
    ciphertext=""
      
    for i in range(len(StringWord)):
        ciphertext += chr((ord(StringWord[i])+intKey-65) % 26+65)
        print((ord(StringWord[i])+intKey-65) % 26+65)
        print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    return plaintext
