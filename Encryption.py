import numpy as np
def caesar_encryption(pt,key):
    l = list(pt)
    ct = []
    ct1=""
    key=key%26
    for i in l:
        
        if i.isupper():
            if ord(i)+key>90: 
                ct.append(chr(ord(i)+key-26))
            else:
                ct.append(chr(ord(i)+key))
        elif ord(i)==32:
            ct.append(' ')

        else:
            if ord(i)+key>122:
                ct.append(chr((ord(i))+key-26))
            else:
                ct.append(chr(ord(i)+key))
    for i in ct:
        ct1+=i;
    return ct1

def vigenere_encryption(pt,key):
    ct=""
    for i in range(len(pt)):
        if pt[i].isupper() and key[i].isupper():
            ct += chr((((ord(pt[i])-65)+(ord(key[i])-65))%26)+65)
        elif ord(pt[i])==32:
            ct+=" "
        elif pt[i].isupper() and key[i].islower():
            ct += chr((((ord(pt[i])-65)+(ord(key[i])-65))%26)+65)
        else:
            ct += chr((((ord(pt[i])-97)+(ord(key[i])-97))%26)+97)   
    return ct


def vernam_encryption(pt,key):
    ct=""
    for i in range(len(pt)):
        if pt[i].isupper() and key[i].isupper():
            ct += chr((((ord(pt[i])-65)+(ord(key[i])-65))%26)+65)
        elif ord(pt[i])==32:
            ct+=" "
        elif pt[i].isupper() and key[i].islower():
            ct += chr((((ord(pt[i])-65)+(ord(key[i])-65))%26)+65)
        else:
            ct += chr((((ord(pt[i])-97)+(ord(key[i])-97))%26)+97)   
    print("Encrypted Message is:",ct)
    
    return ct

def playfare_encryption(pt,key):
    yo=list(pt)
    i=0
    txt=""
    while i<len(yo)-1:
        if yo[i]==yo[i+1]:
            yo.insert(i+1,'X')
            i+=2
        else:
            i+=2
    
    if len(yo)%2==1:
        yo.append('Z')
    pt=[]
    for i in range(0,len(yo),2):
        pt.append(yo[i]+yo[i+1])
    ct=[]
    i=0
    r1,r2,c1,c2=0,0,0,0
    print(pt)
    for i in range(len(pt)):
        for index, row in enumerate(key):
        
            temp=pt[i]
            if temp[0] in row:
                r1,c1=(index, row.index(temp[0]))
            if temp[1] in row:
                r2,c2=(index, row.index(temp[1]))
                
        print("r1",r1,"c1",c1,"r2",r2,"c2",c2)
        if r1 == r2:
            if c1+1>4:
                temp=key[r1][0]+key[r2+1][c2]
            elif c2+1>4:
                temp=key[r1][c1+1]+key[r2][0]
            else:
                temp=key[r1][c1+1]+key[r2][c2+1]
            ct.append(temp)
        elif c1==c2:
            if r1+1>4:
                temp=key[0][c1]+key[r2+1][c2]
            elif r2+1>4:
                temp=key[r1+1][c1]+key[0][c2]
            else:
                temp=key[r1+1][c1]+key[r2+1][c2]
            ct.append(temp)
        else:
            temp=key[r1][c2]+key[r2][c1]
            ct.append(temp)
        
    for i in ct:
        txt+=i
    return txt
    

def playfare_matrix(key):
    a=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]
    
    p=0
    flag=0
    alfa=65
    for i in range(len(a)):
        j=0
        while j!=len(a):
        
        
            if p!=len(key):
                for m in range(len(a)):
                    if key[p].upper() in a[m] and p<len(key):
                        p+=1
                    
                        break
                    elif p<len(key):    
                        a[i][j]=key[p].upper()
                        p+=1
                        j+=1
                        break
            #print(a)
            else:
            #print(j,alfa)
                for m in range(len(a)):
                    if chr(alfa) in a[m]:
                        flag=1
                        break
                    else:
                        flag=0
                if flag!=1 and chr(alfa) != 'J':
                    a[i][j]=chr(alfa)
                    alfa+=1
                    j+=1
                #print(a)
                elif chr(alfa) == 'J':
                    alfa+=1
                    a[i][j]=chr(alfa)
                    j+=1
                else:
                    alfa+=1
    return a

def hill_encryption(pt,key,size,pt2):
    txt=""
    ct=""
    key = np.array(key)
    pt1 = np.array(pt)
    ans = key.dot(pt1)
    ans=np.array(ans)
    ans=ans.transpose()
    for i in ans:
        for j in i:
            txt+=chr(j%26+97)
    
    return txt,ans.transpose()
