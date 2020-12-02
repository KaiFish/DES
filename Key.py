import T

class Key:
    def __init__(self, str):
        self.KP = setKP(str)
        self.c, self.d = setCD(self.KP)
        self.keys = setKeys(self.c, self.d)
        self.KN = setKN(self.keys)

    def setKP(str):
        KP = ""
        for i in T.PC1:
            KP = KP + str[i-1]
        return KP

    def setCD(KP):
        c = []
        d = []
        c0 = KP[:28]
        d0 = KP[28:]
        c.append(c0)
        d.append(d0)
        for i in T.BS:
            for x in range(i):
                c0 = Bits.leftRotate(c0)
                d0 = Bits.leftRotate(d0)
            c.append(c0)
            d.append(d0)
        return c, d

    def setKeys(c, d):
        k = []
        for x, y in zip(c, d):
            k.append(x+y)
        return k

    def setKN(keys):
        KN = []
        for x in keys:
            a = ""
            for i in T.PC2:
                a = a + x[i-1]
            KN.append(a)
        return KN
