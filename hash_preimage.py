import hashlib
import os
import string
import random


def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    x = random.choice(string.ascii_letters)
    x_sha = hashlib.sha256(x.encode('utf-8'))
    final_k_digits_x = bin(int(x_sha.hexdigest(), base=16))[-k:]
    y = random.choice(string.ascii_letters)
    y_sha = hashlib.sha256(y.encode('utf-8'))
    final_k_digits_y = bin(int(y_sha.hexdigest(), base=16))[-k:]

    while final_k_digits_x != final_k_digits_y:
        y += random.choice(string.ascii_letters)
        y_sha = hashlib.sha256(y.encode('utf-8'))
        final_k_digits_y = bin(int(y_sha.hexdigest(), base=16))[-k:]

    byte_x = x.encode('utf-8')
    byte_y = y.encode('utf-8')
    return byte_x, byte_y
