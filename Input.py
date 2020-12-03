import secrets
class Input:
    def __init__(self):
        # print("Single (1) or Triple (3)?")
        # des = int(input())
        # if des == 1:
        #     print("Using Single DES")
        #     self.single = True
        # elif des == 3:
        #     print("Using Triple DES")
        #     self.single = False
        # else:
        #     print("Invalid input, try again")
        #     Input()
        # self.setM()
        # self.setK()
        self.single = True
        self.mS = "hello world"
        self.m = Input.chunk(self.mS)
        self.k1 = Input.generate()


    def setM(self):
        print("Input Message to Encrypt:")
        self.mS = input()
        self.m = Input.chunk(self.mS)

    def setK(self):
        print("Input (o)wn key or auto (g)enerate?")
        opt = input()
        if opt == "o":
            if self.single:
                print("Input Key:")
                self.k1 = DES.sanitize(input())
            else:
                print("Input Key 1:")
                self.k1 = DES.sanitize(input())
                print("Input Key 2:")
                self.k2 = DES.sanitize(input())
        elif opt == "g":
            if self.single:
                self.k1 = Input.generate()
            else:
                self.k1 = Input.generate()
                self.k2 = Input.generate()
        else:
            print("Invalid input, try again")
            self.setK()

    def getK1(self):
        return self.k1

    def getK2(self):
        if self.single:
            return self.k2
        else:
            return null

    def getMessage(self):
        return self.mS

    def chunked(self):
        return self.m

    def isSingle(self):
        return self.single


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
