import numpy as np
import numpy.linalg as m
def modInverse(a, m=26) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def caesar_decryption(ct,key):
    key=key%26
    ct=list(ct)
    pt=[]
    txt=""
    for i in ct:
        if i.isupper():
            if (ord(i)-key)<65:
                pt.append(chr(ord(i)-key+26))
            else:
                pt.append(chr(ord(i)-key))
        elif ord(i)==32:
            pt.append(' ')
        else:
            if (ord(i)-key)<97:
                pt.append(chr(ord(i)-key+26))
            else:
                pt.append(chr(ord(i)-key))
    for i in pt:
        txt+=i
    return txt
def vigenere_decryption(ct,key):
    pt=""
    for i in range(len(ct)):
        if ct[i].isupper():
            if (ord(ct[i])-65)-(ord(key[i])-65)<0:
                pt += chr((((ord(ct[i])-65)-(ord(key[i])-65)+26)%26)+65)
            else:
                pt += chr((((ord(ct[i])-65)-(ord(key[i])-65))%26)+65)
        elif ord(ct[i])==32:
            ct+=" "
        else:
            if (ord(ct[i])-97)-(ord(key[i])-97)<0:
                pt += chr((((ord(ct[i])-97)-(ord(key[i])-97)+26)%26)+97)
            else:
                pt += chr((((ord(ct[i])-97)-(ord(key[i])-97))%26)+97)
    return pt

def vernam_decryption(ct,key):
    pt=""
    for i in range(len(ct)):
        if ct[i].isupper():
            if (ord(ct[i])-65)-(ord(key[i])-65)<0:
                pt += chr((((ord(ct[i])-65)-(ord(key[i])-65)+26)%26)+65)
            else:
                pt += chr((((ord(ct[i])-65)-(ord(key[i])-65))%26)+65)
        elif ord(ct[i])==32:
            ct+=" "
        else:
            if (ord(ct[i])-97)-(ord(key[i])-97)<0:
                pt += chr((((ord(ct[i])-97)-(ord(key[i])-97)+26)%26)+97)
            else:
                pt += chr((((ord(ct[i])-97)-(ord(key[i])-97))%26)+97)
    return pt

def playfare_decryption(ct1,key):
    pt=[]
    ct=[]
    txt=""
    for i in range(0,len(ct1),2):
        ct.append(ct1[i]+ct1[i+1])
    for i in range(len(ct)):
        for index, row in enumerate(key):
        
            temp=ct[i]
            if temp[0] in row:
                r1,c1=(index, row.index(temp[0]))
            if temp[1] in row:
                r2,c2=(index, row.index(temp[1]))
                
        if r1 == r2:
            if c1-1<0:
                temp=key[r1][4]+key[r2][c2-1]
            elif c2-1<0:
                temp=key[r1][c1-1]+key[r2][4]
            else:
                temp=key[r1][c1-1]+key[r2][c2-1]
            pt.append(temp)
        elif c1==c2:
            if r1-1<0:
                temp=key[4][c1]+key[r2-1][c2]
            elif r2-1<0:
                temp=key[r1-1][c1]+key[4][c2]
            else:
                temp=key[r1-1][c1]+key[r2-1][c2]
            pt.append(temp)
        else:
            temp=key[r1][c2]+key[r2][c1]
            pt.append(temp)
    for i in pt:
        txt+=i

    return txt
def hill_decryption(ct,key): 
    txt=""
    key=np.array(key)
    d=round(m.det(key))
    key=np.linalg.inv(key)
    
    for i in range(len(key)):
        for j in range(len(key)):
            key[i][j]=(key[i][j]*d)
    modInverse(d)
    if d==1:
        return 'Mod is not possible'
    elif d<0 or d>26:
        d=d%26
        
        for i in range(len(key)):
            for j in range(len(key)):
                key[i][j]=(key[i][j]*d)%26
            
        
    else:
        for i in range(len(key)):
            for j in range(len(key)):
                key[i][j]=int(key[i][j]*d)
    
    ans=key.dot(ct)
    ans=ans.transpose()
    
    for i in ans:
        for j in i:
            txt+=chr(int(round(j)%26+97))
    return txt

    
    

    