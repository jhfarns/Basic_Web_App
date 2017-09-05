import string,random

def random (length = 8, string =  string.ascii_uppercase + string.digits):
    return ''.join(random.choice(string) for a in range(length))
