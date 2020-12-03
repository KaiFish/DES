#key.py @author Kai Barclay 2020

import T
from bits import leftRotate

#this class takes an initial key and aquires the complete keyset from it

class Key:
    def __init__(self, str):
        assert len(str) == 64   #64 bit key required for DES
        self.keys = setKN(setKeys(*setCD(setKP(str)))) #final key set

    def getKeys(self):  #returns final key set
         return self.keys

    def invert(self):   #reverse keyset for decryption
        self.keys.reverse()

def setKP(str): #uses permuted-choice-1 to get K+
    KP = ""
    for i in T.PC1:
        KP = KP + str[i-1]
    return KP

def setCD(KP): #gets all c and d half keys, through left rotations
    cs = []
    ds = []
    c0 = KP[:28] #c0 is left half
    d0 = KP[28:] #d0 is right half
    cs.append(c0)
    ds.append(d0)
    for i in T.BS:
        for x in range(i): #always 1 or 2, based on bit shift table
            c0 = leftRotate(c0)
            d0 = leftRotate(d0)
        cs.append(c0)
        ds.append(d0)
    return cs, ds

def setKeys(c, d): #combines c and d blocks to get keys
    k = []
    for x, y in zip(c, d):
        k.append(x+y)
    return k

def setKN(keys): #uses permuted-choice-2 to get Kn set
    KN = []
    for x in keys:
        a = ""
        for i in T.PC2:
            a = a + x[i-1]
        KN.append(a)
    KN = KN[1:] #K0 is unused, remove to avoid off-by one errors
    return KN
