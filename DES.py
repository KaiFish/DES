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

def DES(m, k):          #base encryption given message, key
    if str.isdecimal(m) == False:
        c = chunk(m)
    else:
        c = chop(m)
    key = Key(k)
    encrypt = ""
    for i in range(len(c)):
        math = Mafs(c[i], key)
        encrypt = encrypt + math.getFP()
    return encrypt

def unDES(m, k):        #base decryption given ciphertext (in binary), key
    key = Key(k)
    c = chop(m)
    key.invert()
    decrypt = ""
    for i in range(len(c)):
        math = Mafs(c[i], key)
        decrypt = decrypt + math.getFP()
    return decrypt

def DES3(m, k1, k2):
    return DES(unDES(DES(m, k1), k2), k1)

def unDES3(m, k1, k2):
    return unDES(DES(unDES(m, k1), k2), k1)

def chop(x):            #splits binary string into list of 64 bit chunks
    split = []
    while x != "":
        s = ""
        for i in range(64):
            if x != "":
                s = s + x[0]
                x = x[1:]
        split.append(s)
    return split


if __name__ == '__main__':
    main()
