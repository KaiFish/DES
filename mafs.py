#mafs.py @author Kai Barclay 2020

import numpy as np
import T
from bits import *

#this class, given a message and an initial key, performs the Fiestel functions

class Mafs: #cheers to my british friends and their lovely way of saying things
    def __init__(self, m, k):
        self.m = m
        self.k = k.getKeys() #gets the key set
        #together, this makes the Fiestel structure
        self.FP = setFP(setRL(setIP(self.m), self.k))

    def getFP(self): #returns the results of the final permutation
        return self.FP


def setIP(str): #performs initial permutation on message
    IP = ""
    for i in T.IP:
        IP = IP + str[i-1]
    return IP

def setRL(IP, k): #gets the final r16l16 result
    l = []
    r = []
    l.append(IP[:32]) #l0
    r.append(IP[32:]) #r0
    for i in range(16):
        l.append(r[i]) #ln = rn-1
        r.append(xor(l[i], feistel(r[i], k[i]))) #rn = ln-1 ^ f(rn-1, kn-1)
    rl = "" + r[16] + l[16] #combine r16 with l16
    return rl

def setFP(rl):  #performs final permutation on text
    f = ""
    for i in T.FP:
        f = f + rl[i-1]
    return f

def expand(x): #expands x from 32 bits to 48 bits
    e = ""
    for i in T.E:
        e = e + x[i-1]
    return e

def split(x):   #splits x into 8 6-bit pieces
    split = []
    while x != "":
        s = ""
        for i in range(6):
            s = s + x[0]
            x = x[1:]
        split.append(s)
    return split

def getIJ(x):   #given 6-bit x, bits 0 & 5 make i, bits 1-4 make j
    i = x[0] + x[5]
    j = x[1:5]
    return int(i, 2), int(j, 2)

def setS(x): #perform S box substitutions
    s = ''
    for a, b in zip(x, T.S):
        i, j = getIJ(a)
        c = b[i, j] #get value from given S-Box
        d = toBits(c, 4) #convert to 4 bits
        s = s + d
    return s

def setP(x): #perform permutation of x
    p = ""
    for i in T.P:
        p = p + x[i-1]
    return p

def feistel(f, k): #perform one Fiestel operation
    e = expand(f)
    x = xor(e, k)
    s = setS(split(x))
    p = setP(s)
    return p
