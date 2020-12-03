#user.py @author Kai Barclay 2020

import secrets
import sys

#this class handles initial/important user input

class User:
    def __init__(self):
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        crypt = input()
        if crypt == 'e':
            self.encrypt = True     #encrypting
        elif crypt == 'd':
            self.encrypt = False    #decrypting
        elif crypt == 'q':
            sys.exit(0)             #exit program
        else:
            print("Invalid input, try again")
            Input()                 #gotta get that input
        print("Single (1) or Triple (3) DES?")
        des = int(input())
        if des == 1:
            print("Using Single DES")
            self.single = True      #single DES
        elif des == 3:
            print("Using Triple DES")
            self.single = False     #triple DES
        else:
            print("Invalid input, try again")
            User()
        self.setM()         #get plain/cipher text to use
        self.setK()         #get keys

    def setM(self): #get plain/cipher text to use
        if self.encrypt:
            print("Input Message to Encrypt:")
        else:
            print("Input Message to Decrypt:")
            print("(currently can handle binary and alpha(?) strings)")
            #it's most tested with decrypting from binary
        self.mS = input()

    def setK(self):
        if self.encrypt:    #if encrypting
            print("Input (o)wn key or auto (g)enerate?")
            opt = input()
            if opt == "o":      #user will provide key(s)
                print("Warning: Keys are ensured to be 64 bits. Your key will be modified if it is not 64 bits.")
                #ie: don't trust users
                if self.single == True:
                    print("Input Key:")
                    self.k1 = sanitize(input())
                else:
                    print("Input Key 1:")
                    self.k1 = sanitize(input())
                    print("Input Key 2:")
                    self.k2 = sanitize(input())
            elif opt == "g":    #program will generate key(s)
                if self.single == True:
                    self.k1 = generate()
                else:
                    self.k1 = generate()
                    self.k2 = generate()
            else:
                print("Invalid input, try again")
                self.setK()
        else:#if decrypting, user must provide key(s), hope they do it right
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

    def getK1(self):    #return key 1
        return self.k1

    def getK2(self):    #return key2 if it exists
        if self.single == False:
            return self.k2
        else:
            return None

    def getMessage(self):   #return user provided text
        return self.mS

    def isSingle(self):     #is single DES?
        return self.single

    def isEncryption(self): #is encrypting?
        return self.encrypt


def charToBits(c):  #converts ascii to 8-bit binary
    b = format(ord(c), 'b') #standard ascii is 7-bit
    while len(b) < 8:       #this pads with leading 0s to make it 8-bit
        b = '0' + b
    return b

def chunk(m):   #converts binary string to 64-bit chunks in list
    chunks = []
    while m != "":
        s = ""
        for x in range(8):
            if m != "":
                s = s + charToBits(m[0])
                m = m[1:]
            else:
                while len(s) < 64:  #pads with end of text symbol to make even
                    s = s + '00000011'
        chunks.append(s)
    return chunks

def sanitize(key):  #make sure user is not stupid
    b = ''
    if str.isdecimal(key) == False:
        for c in key:
            b = b + charToBits(c)
    else:
        b = b + key
    if len(b) < 64:               # pad given key if too short
        x = 64 - len(b)
        b = b + format(secrets.randbits(x), 'b')
    elif len(b) > 64:             # cut given key if too long
        b = b[0:63]
    return b

def generate(): #generate random key
    key = secrets.randbits(64)
    x = format(key, 'b')
    while len(x) < 64:
        x = '0' + x
    assert len(x) == 64
    return x
