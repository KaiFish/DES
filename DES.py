from Input import *
from Key import Key
from Mafs import Mafs
import Bits

def main():
    i = Input()
    k1 = Key(i.getK1())
    if i.isSingle() != True:
        k2 = Key(i.getK2())
    print("Message is " + i.getMessage())
    encrypt = ""
    for m in i.chunked():
        math = Mafs(m, k1)
        encrypt = encrypt + math.getFP()
    print("Encrypted as " + encrypt)
    print("Decrypting...")
    c = Input.chunk(encrypt)
    k1.invert()
    decrypt = ""
    for x in c:
        math = Mafs(x, k1)
        decrypt = decrypt + math.getFP()
    print("Decrypted as " + Bits.toChar(decrypt))

def DES(m, k):
    c = chunk(m)
    key = Key(k)
    encrypt = ""
    for i in c:
        math = Mafs(i, key)
        encrypt = encrypt + math.getFP()
    return encrypt

def unDES(m, k):
    key = Key(k)
    c = chop(m)
    key.invert()
    decrypt = ""
    for i in c:
        math = Mafs(i, key)
        decrypt = decrypt + math.getFP()
    return decrypt

def chop(x):
    split = []
    while x != "":
        s = ""
        for i in range(64):
            s = s + x[0]
            x = x[1:]
        split.append(s)
    return split


if __name__ == '__main__':
    main()
