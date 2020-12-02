import codecs
import secrets
import numpy as np
import DES

#Permuted Choice 1
PC1 =   [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permuted Choice 2
PC2 =   [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]

#Bit Shift
BS =    [1, 1, 2, 2, 2, 2, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 1]

#Initial Permutation
IP =    [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

#Final Permutation (Inverse of Initial Permutation)
FP =    [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Expansion Function
E =     [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]

#Permutation
P =     [16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25]

#Substitution Blocks 1-8
S1 = np.array(  [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]], dtype=int)

S2 = np.array(  [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]], dtype=int)

S3 = np.array(  [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]], dtype=int)

S4 = np.array(  [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 7],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]], dtype=int)

S5 = np.array(  [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]], dtype=int)

S6 = np.array(  [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 1],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]], dtype=int)

S7 = np.array(  [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]], dtype=int)

S8 = np.array(  [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]], dtype=int)

class DES:

    def __init__(self):
        print("Single (1) or Triple (3)?")
        self.des = int(input())
        self.mS = ""
        self.m = []
        self.k1 = []
        if self.des == 1:
            print("Using Single DES")
        elif self.des == 3:
            print("Using Triple DES")
            self.k2 = []
        else:
            print("Invalid input, try again")
            DES()
        self.getK()
        self.getM()

    def sanitize(key):
        if len(key) < 64:               # pad given key if too short
            x = 64 - len(key)
            key = key + secrets.randbits(x)
        elif len(key) > 64:             # cut given key if too long
            key = key[0:63]

        key = key.to_bytes(8, byteorder='big')
        return key

    def generate(self):
        key = secrets.randbits(64)
        key = key.to_bytes(8, byteorder='big')
        return key

    def chunkIt(m):
        chunks = []
        while m != "":
            s = ""
            for x in range(8):
                if m != "":
                    s = s + m[0]
                    m = m[1:]
                else:
                    s = s + " "
            s = s.to_bytes(8, byteorder = 'big')
            chunks.append(s)
        return chunks

    def getM(self):
        print("Input Message to Encrypt:")
        self.mS = input()
        self.m = self.chunkIt(self.mS)

    def getK(self):
        print("Input (o)wn key or auto (g)enerate?")
        opt = input()
        if opt == "o":
            if self.des == 1:
                print("Input Key:")
                self.k1 = DES.sanitize(input())
            elif self.des == 3:
                print("Input Key 1:")
                self.k1 = DES.sanitize(input())
                print("Input Key 2:")
                self.k2 = DES.sanitize(input())
        elif opt == "g":
            if self.des == 1:
                self.k1 = self.generate()
            elif self.des == 3:
                self.k1 = self.generate()
                self.k2 = self.generate()
        else:
            print("Invalid input, try again")
            self.getK()

class Mafs:

    def __init__(self):
        self.des = DES()
        setUp()
        print("let's do some mafs")

    def setUp(self):
        self.KP = getKP(1)
        self.c, self.d = getCD(KP)
        self.KN = getKN(getKeys(c, d))
        if self.DES.des == 3:
            self.KP2 = getKP(2)
            self.c2, self.d2 = getCD(KP2)
            self.KN2 = getKN(getKeys(c2, d2))

    def getKP(self, keyNum):
        KP = []
        for i in PC1:
            if keyNum == 1:
                KP.append(self.DES.k1[i])
            elif keyNum == 2:
                KP.append(self.DES.k2[i])
        return KP

    def getCD(key):
        c = []
        d = []
        c0 = key[:28]
        d0 = key[28:]
        c.append(c0)
        d.append(d0)
        for i in BS:
            for x in range(i):
                a = c0.pop()
                b = d0.pop()
                c0.append(a)
                d0.append(b)
            c.append(c0)
            d.append(d0)
        return c, d

    def getKeys(c, d):
        k = []
        for x, y in zip(c, d):
            k.append(x+y)
        return k

    def getKN(self, keys):
        KN = []
        for x in keys:
            a = []
            for i in PC2:
                a.append(x[i])
            KN.append(a)
        return KN;


if __name__ == '__main__':
    Mafs()
