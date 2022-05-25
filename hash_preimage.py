import hashlib
import os

def hash_preimage(target_string):

    from hashlib import sha256
    from random import randrange

    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    k = len(target_string)
    upper_bound = round(pow(2,k),0)

    seed = str(randrange(upper_bound))
    byte_seed = seed.encode('utf-8')
    x = byte_seed
    flag = 0

    b_target = target_string.encode('utf-8')
    
    while (flag==0):
        for i in range(k):
            h_variable = sha256(x).hexdigest()
            b_variable = "{0:08b}".format(int(h_variable, 16))
            if ((target_string)[-k:] == (b_variable)[-k:]):
                flag=1
                break
            else:
                x = int(x)
                x=x+randrange(upper_bound)
                x = str(x).encode('utf-8')

    x=bytes(x)
    return( x )

# The python interpreter actually executes the function body here
print("Answer: ")
hash_preimage("01")
