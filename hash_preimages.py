import hashlib
import string
import random

def hash_preimage(target_string):
    if not isinstance(target_string, str):
        print( "Input need to be a string" )
        return
        
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    k = len(target_string)
    if k > 256:
        print( "Input is too long" )
        return
    
    notEqual = True
    end_length = 256
    while(notEqual):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        hx = hashlib.sha256(x)
        hx16 = hx.hexdigest()
        hx2 = bin(int(hx16, 16))[2:].zfill(end_length)
        hx_trailing = hx2[-k:]
        if hx_trailing == target_string:
            notEqual = False

    return( x )
