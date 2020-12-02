import numpy as np

class Mafs:
    def __init__(self, m, k):
        self.m = m
        self.k = k.getKeys()
        self.FP = getFP(getRL(getIP(self.m), self.k))

    def getIP(str):
        IP = ""
        for i in T.IP:
            IP = IP + str[i-1]
        return IP

    def getRL(IP, k):
        l = []
        r = []
        l.append(IP[:32])
        r.append(IP[32:])
        for i in range(16):
            l.append(r[i])
            r.append(Bits.xor(l[i], fiestel(r[i], k[i])))
        rl = "" + r[15] + l[15]
        return rl

    def getFP(rl):
        f = ""
        for i in T.FP:
            f = f + rl[i-1]
        return f

    def expand(x):
        e = ""
        for i in T.E:
            e = e + x[i-1]
        return e

    def split(x):
        split = []
        while x != "":
            s = ""
            for i in range(6):
                s = s + x[0]
                x = x[1:]
            split.append(s)
        return split

    def getIJ(x):
        i = x[0] + x[5]
        j = x[1:5]
        return int(i, 2), int(j, 2)

    def getS(x):
        s = ''
        for a, b in zip(x, T.S):
            i, j = Mafs.getIJ(a)
            c = b[i, j]
            d = Bits.toBits(c, 4)
            s = s + d
        return s

    def getP(x):
        p = ""
        for i in T.P:
            p = p + x[i-1]
        return p

    def feistel(f, k):
        e = expand(f)
        x = Bits.xor(e, k)
        s = getS(split(x))
        p = getP(s)
        return p

    def getFP(self):
        return self.FP
