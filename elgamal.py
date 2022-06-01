from elgamal_util import mod_inverse
import random

from params import p
from params import g

# returns secret key [1..p] and public key g^a mod p
def keygen():
    q = mod_inverse(g, p)    # q is the order of g
    a = random.SystemRandom().randint(1, q)
    h = pow(g,a,p)
    sk = a
    pk = h
    return pk,sk

# take public key, h, and integer, m, and return an El Gamal ciphertext
def encrypt(pk,m):
    q = mod_inverse(g, p)
    r = random.SystemRandom().randint(1, q)
    c1 = pow(g,r,p)
    c2 = pow( (pow(pk,r,p) * pow(m,1,p)), 1, p )
    return [c1,c2]

# take private key, a, and ciphertext [c1,c2] and return an integer m
# (𝑎*𝑏 % 𝑚)=((𝑎 % 𝑚)*(𝑏 % 𝑚)) % 𝑚

# Modular exponentiation can be performed with a negative 
# exponent e by finding the modular multiplicative 
# inverse d of b modulo m using the extended Euclidean 
# algorithm. That is: 
# c = b^e mod m 
#   = d^−e mod m, where d ⋅ b ≡ 1 (mod m). => need inverse of (d, m)
# d = c[0] and e = sk, m = p
# b^sk mod p

# Given two integers ‘a’ and ‘m’, 
# The modular multiplicative inverse is an integer ‘x’ 
# such that. a ⋅ x ≅ 1 (mod m) 
def decrypt(sk,c):
    t2=pow(c[1],1,p)
    x = mod_inverse(c[0],p)
    t1 = pow(x, sk, p)
    m = pow(t2*t1,1,p)
    print(m)
    return m
