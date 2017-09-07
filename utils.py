from os import urandom

def random_string(length = 16):
    return urandom(length / 2).encode('hex')
