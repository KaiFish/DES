MAX = 2**64-1

def ones(n):
    return MAX >> (64-n)

def num(str):
    return int(str, 2)

def numBits(str):
    return len(bin(int(str, 2))) - 2

def leftRotate(key):
    n = num(key)
    b = numBits(key)
    x = (n << 1) | (n >> (b-1))
    x = x & ones(b)
    s = format(x, 'b')
    while len(s) < b:
        s = '0' + s
    return s
