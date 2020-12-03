import T
import Bits

class Key:
    def __init__(self, str):
        assert len(str) == 64
        self.keys = Key.setKN(Key.setKeys(*Key.setCD(Key.setKP(str))))

    def setKP(str):
        KP = ""
        for i in T.PC1:
            KP = KP + str[i-1]
        return KP

    def setCD(KP):
        cs = []
        ds = []
        c0 = KP[:28]
        d0 = KP[28:]
        cs.append(c0)
        ds.append(d0)
        for i in T.BS:
            for x in range(i):
                c0 = Bits.leftRotate(c0)
                d0 = Bits.leftRotate(d0)
            cs.append(c0)
            ds.append(d0)
        return cs, ds

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

    def getKeys(self):
         return self.keys

    def invert(self):
        self.keys.reverse()
