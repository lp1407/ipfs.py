import hashlib
import os
import string
import random

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    #Collision finding code goes here
    letters = string.ascii_letters
    newString = ''.join(random.choice(letters) for i in range(256))
    x = newString.encode('utf-8')
    
    invCollide = 0
    while (invCollide == 0):
        hashX = hashlib.sha256(x).digest()
        intX = int.from_bytes(hashX, 'big')
        binX = bin(intX)
        if (binX[(len(binX) - len(target_string)):] == target_string):
            isCollision = 1
        else:
            newString = ''.join(random.choice(letters) for i in range(256))
            x = newString.encode('utf-8')

    imnone = x

    return( imnone )
