#bits.py @author Kai Barclay 2020
#all of the binary based functions for the program

MAX = 2**64-1

def ones(n):    #returns n-bits of 1s
    return MAX >> (64-n)

def num(str):   #returns a binary string as an int
    return int(str, 2)

def numBits(str):   #returns number of bits in binary string
    return len(str)

def leftRotate(key):    #performs a left rotation on given binary string
    n = num(key)
    b = numBits(key)
    x = (n << 1) | (n >> (b-1))
    x = x & ones(b)
    s = toBits(x, b)
    return s

def xor(e, k):  #xors and formats given binary strings
    a = num(e)
    b = num(k)
    c = numBits(e)
    x = a ^ b
    s = toBits(x, c)
    return s

def toBits(num, bits):  #formats an int as a binary string with bits-bits
    s = format(num, 'b')
    while len(s) < bits:
        s = '0' + s
    return s

def toChar(bin):   #converts a binary string to its (8-bit) ascii representation
    s = ""
    while bin != "":
        x = bin[0:8]
        s = s + chr(int(x, 2))
        bin = bin[8:]
    return s
