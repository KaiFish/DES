import secrets
import sys

class Input:
    def __init__(self):
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        crypt = input()
        if crypt == 'e':
            self.encrypt = True
        elif crypt == 'd':
            self.encrypt = False
        elif crypt == 'q':
            sys.exit(0)
        else:
            print("Invalid input, try again")
            Input()
        print("Single (1) or Triple (3) DES?")
        des = int(input())
        if des == 1:
            print("Using Single DES")
            self.single = True
        elif des == 3:
            print("Using Triple DES")
            self.single = False
        else:
            print("Invalid input, try again")
            Input()
        self.setM()
        self.setK()
        # self.single = True
        # self.mS = "hello world"
        # self.m = Input.chunk(self.mS)
        # self.k1 = Input.generate()


    def setM(self):
        if self.encrypt:
            print("Input Message to Encrypt:")
        else:
            print("Input Message to Decrypt:")
            print("(currently can handle binary and alpha strings)")
        self.mS = input()

    def setK(self):
        if self.encrypt:
            print("Input (o)wn key or auto (g)enerate?")
            opt = input()
            if opt == "o":
                print("Warning: Keys are ensured to be 64 bits. Your key will be modified if it is not 64 bits.")
                if self.single:
                    print("Input Key:")
                    self.k1 = sanitize(input())
                else:
                    print("Input Key 1:")
                    self.k1 = sanitize(input())
                    print("Input Key 2:")
                    self.k2 = sanitize(input())
            elif opt == "g":
                if self.single:
                    self.k1 = generate()
                else:
                    self.k1 = generate()
                    self.k2 = generate()
            else:
                print("Invalid input, try again")
                self.setK()
        else:
            print("Provide key(s) to use:")
            print("Warning: Key must be 64 bits for proper decryption!")
            if self.single:
                print("Input Key:")
                self.k1 = sanitize(input())
            else:
                print("Input Key 1:")
                self.k1 = sanitize(input())
                print("Input Key 2:")
                self.k2 = sanitize(input())

    def getK1(self):
        return self.k1

    def getK2(self):
        if self.single:
            return self.k2
        else:
            return null

    def getMessage(self):
        return self.mS

    def isSingle(self):
        return self.single

    def isEncryption(self):
        return self.encrypt


def charToBits(c):
    b = format(ord(c), 'b')
    while len(b) < 8:
        b = '0' + b
    return b

def chunk(m):
    chunks = []
    while m != "":
        s = ""
        for x in range(8):
            if m != "":
                s = s + charToBits(m[0])
                m = m[1:]
            else:
                while len(s) < 64:
                    s = s + '00000011'
        chunks.append(s)
    return chunks

def sanitize(key):
    b = ''
    for c in key:
        b = b + charToBits(c)
    if len(b) < 64:               # pad given key if too short
        x = 64 - len(b)
        b = b + secrets.randbits(x)
    elif len(b) > 64:             # cut given key if too long
        b = b[0:63]
    return b

def generate():
    key = secrets.randbits(64)
    x = format(key, 'b')
    while len(x) < 64:
        x = '0' + x
    assert len(x) == 64
    return x
