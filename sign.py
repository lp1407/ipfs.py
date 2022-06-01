from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

# The high level verify algorithm is to take your public key, message, 
# and signature and ensure that the output of sign_pk(msg) = signature

def sign(m):
    #generate public key
    str_m = str(m)
    byte_m = str_m.encode('utf-8')
    private_key, public_key = keys.gen_keypair(curve.secp256k1) 
    #generate signature
    r, s = ecdsa.sign(byte_m, private_key, curve.secp256k1, sha256)
    return( public_key, [r,s] )
