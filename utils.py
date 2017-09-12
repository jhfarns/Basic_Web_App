from os import urandom
import random
import sys
from binascii import hexlify

def random_string(length = 16):
    return str(hexlify(urandom(length // 2)), 'ascii')

def random_number():
    key_num = random.SystemRandom()
    return key_num.randint(0, 999999999999999999)
