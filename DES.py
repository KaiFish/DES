#DES.py @author Kai Barclay 2020
#main method here
#run this as: python3 DES.py

from user import User
from user import *
from key import Key
from mafs import Mafs
from bits import *
import sys

def main():     #program flow
    print("Welcome to DES.")
    end = False
    while end == False:
        i = User()
        if i.isEncryption() == True:    #Encrypting
            print("Encrypting....")
            print("Message: " + i.getMessage())
            if i.isSingle() == True:        #single DES
                print("Key: " + i.getK1())
                e = DES(i.getMessage(), i.getK1())
                print("Cipher: " + e)
                end = option1(e, i)
            else:                           #triple DES
                print("Key 1:  " + i.getK1())
                print("Key 2:  " + i.getK2())
                e = DES3(i.getMessage(), i.getK1(), i.getK2())
                print("Cipher: " + e)
                end = option1(e, i)
        else:                           #Decrypting
            print("Decrypting....")
            print("Cipher Text: " + i.getMessage())
            if i.isSingle() == True:        #single DES
                print("Key: " + i.getK1())
                u = unDES(i.getMessage(), i.getK1())
                print("Plain Text: " + toChar(u))
                end = option2()
            else:                           #triple DES
                print("Key 1: " + i.getK1())
                print("Key 2: " + i.getK2())
                e = DES3(i.getMessage(), i.getK1(), i.getK2())
                print("Cipher: " + e)
                end = option2()


def DES(m, k):          #encryption given message, key
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

def unDES(m, k):        #decryption given ciphertext (in binary or alpha), key
    key = Key(k)
    if str.isdecimal(m) == False:
        c = chunk(m)
    else:
        c = chop(m)
    key.invert()
    decrypt = ""
    for i in range(len(c)):
        math = Mafs(c[i], key)
        decrypt = decrypt + math.getFP()
    return decrypt

def DES3(m, k1, k2): #triple DES encryption
    return DES(unDES(DES(m, k1), k2), k1)

def unDES3(m, k1, k2): #triple DES decryption
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

def option1(e, i): #user menu A
    x = 'a'
    end = False
    while x == 'a':
        print("Do you wish to (d)ecipher, (r)estart, or (q)uit?")
        x = input()
        if x == 'd':
            print("Decrypting....")
            if i.isSingle():
                d = unDES(e, i.getK1())
            else:
                d = unDES3(e, i.getK1(), i.getK2())
            print("Deciphered: " + toChar(d))
        elif x == 'r':
            break
        elif x == 'q':
            sys.exit(0)
        else:
            print("Invalid input, try again")
            x = 'a'
    return end

def option2(): #user menu B
    x = 'a'
    end = False
    while x == 'a':
        print("Do you wish to (r)estart, or (q)uit?")
        x = input()
        if x == 'r':
            break
        elif x == 'q':
            sys.exit(0)
        else:
            print("Invalid input, try again")
            x = 'a'
    return end

if __name__ == '__main__':
    main()
