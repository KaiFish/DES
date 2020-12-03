MAX = 2**64-1

def ones(n):
    return MAX >> (64-n)

def num(str):
    return int(str, 2)

def numBits(str):
    return len(str)

def leftRotate(key):
    n = num(key)
    b = numBits(key)
    x = (n << 1) | (n >> (b-1))
    x = x & ones(b)
    s = toBits(x, b)
    return s

def xor(e, k):
    a = num(e)
    b = num(k)
    c = numBits(e)
    x = a ^ b
    s = toBits(x, c)
    return s

def toBits(num, bits):
    s = format(num, 'b')
    while len(s) < bits:
        s = '0' + s
    return s

def toChar(bin):
    s = ""
    while bin != "":
        x = bin[0:8]
        s = s + chr(int(x, 2))
        bin = bin[8:]
    return s
