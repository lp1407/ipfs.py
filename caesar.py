def encrypt(key, plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        wordHolder = plaintext[i]

        ciphertext += chr((ord(wordHolder)+key-65) % 26+65)
       
    return ciphertext

def decrypt(key,ciphertext):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for letter in ciphertext:
        if letter in alpha:
          
            letter_index = (alpha.find(letter) - key) % len(alpha)

            plaintext = plaintext + alpha[letter_index]
        print(plaintext)
    return plaintext
