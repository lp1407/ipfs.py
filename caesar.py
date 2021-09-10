def encrypt(StringWord, intKey):
    ciphertext = ""
    for i in range(len(StringWord)):
        wordHolder = StringWord[i]

        ciphertext += chr((ord(wordHolder)+intKey-65) % 26+65)
        print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    return plaintext
