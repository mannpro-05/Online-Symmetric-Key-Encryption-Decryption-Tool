from flask import *
from Encryption import *
from Decryption import *
from random import *
from string import *
import numpy as np
app  =  Flask(__name__)

@app.route('/')
def default():
    return render_template("index.html")
@app.route('/caesar_cipher')
def caesar():
    return render_template("caesar_cipher.html",text = 'Output',suggestion = 'Please Enter The Values')
@app.route('/vigener_cipher')
def vigener():
    return render_template("vigener_cipher.html",text = 'Output',suggestion = 'Please Enter The Values')

@app.route('/vernam_cipher')
def vernam():
    return render_template("vernam_cipher.html",text = 'Output',suggestion = 'Please Enter The Values')

@app.route('/playfare_cipher')
def playfare():
    return render_template("playfare_cipher.html",text = 'Output',suggestion = 'Please Enter The Values')

@app.route('/hill_cipher')
def hill():
    return render_template("hill_cipher.html",text = 'Output',suggestion = 'Please Enter The Values')


@app.route('/caesar_cipher_encryption',methods = ['POST','GET'])
def default1():
    if request.method == 'POST':
        pt = request.form['frm_pt']
        key = int(request.form['frm_key'])
        ct = caesar_encryption(pt,key)

        return render_template('caesar_cipher.html',ct = ct,pt = pt,key = key,text = "Encrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")
    else:
        return render_template("caesar_cipher.html",text = 'failure')

@app.route('/caesar_cipher_decryption',methods = ['POST','GET'])
def default2():
    if request.method == 'POST':
        ct = request.form['frm_pt']
        key = int(request.form['frm_key'])
        pt = caesar_decryption(ct,key)

        return render_template('caesar_cipher.html',ct = pt,pt = ct,key = key,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")
    else:
        return render_template("caesar_cipher.html",text = 'failure')

@app.route('/vigener_cipher_encryption',methods = ['POST','GET'])
def encryption_vigener():
    if request.method == 'POST':
        pt = request.form['frm_pt']
        key = request.form['frm_key']
        if len(pt)<=len(key):
            key = key[:len(pt)]
        else:
            i = len(key)
            length = len(key)
            while(i != len(pt)):
                key += key[i%length]
                i += 1

        ct = vigenere_encryption(pt,key)
        return render_template('vigener_cipher.html',ct = ct,key = key,pt = pt,text = "Encrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")

@app.route('/vigener_cipher_decryption',methods = ['POST','GET'])
def decryption_vigener():
    if request.method == 'POST':
        ct = request.form['frm_pt']
        key = request.form['frm_key']
        if len(ct) <= len(key):
            key = key[:len(ct)]
        else:
            i = len(key)
            length = len(key)
            while(i != len(ct)):
                key += key[i%length]
                i += 1

        pt = vigenere_decryption(ct,key)
        return render_template('vigener_cipher.html',ct = pt,key = key,pt = ct,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")

@app.route('/vernam_cipher_encryption',methods = ['POST','GET'])
def encryption_vernam():
    if request.method == 'POST':
        pt = request.form['frm_pt']
        key = ''

        for i in range(len(pt)):
            key+=''.join(choice(ascii_letters))

        ct = vernam_encryption(pt,key)
        return render_template('vernam_cipher.html',ct = ct,key = key,pt = pt,text = "Encrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")

@app.route('/vernam_cipher_decryption',methods = ['POST','GET'])
def decryption_vernam():
    if request.method == 'POST':
        ct = request.form['frm_pt']
        key = request.form['frm_key']
        pt = vernam_decryption(ct,key)
        return render_template('vernam_cipher.html',ct = pt,key = key,pt = ct,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")

@app.route('/playfare_cipher_encryption',methods = ['POST','GET'])
def encryption_playfare():
    if request.method == 'POST':
        pt = request.form['frm_pt']
        pt = pt.upper()
        key = request.form['frm_key']
        key = playfare_matrix(key)

        ct  =  playfare_encryption(pt,key)

        return render_template('playfare_cipher.html',ct = ct,key = key,pt = pt,text = "Encrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")

@app.route('/playfare_cipher_decryption',methods = ['POST','GET'])
def decryption_playfare():
    if request.method == 'POST':
        ct  =  request.form['frm_pt']
        key  =  request.form['frm_key']
        key1  =  request.form['frm_key']
        key  =  playfare_matrix(key)
        pt = playfare_decryption(ct,key)
        return render_template('playfare_cipher.html',ct = pt,key = key,key1 = "This is the key matrix which is generated by the key:"+key1,pt = ct,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!")
@app.route('/hill_cipher_encryption',methods = ['POST','GET'])
def encryption_hill():
    if request.method == 'POST':
        pt1=[]
        key=[]
        pt  =  request.form['frm_pt']
        size = int(request.form['inp'])
        for i in range(size):
            p=[]
            for j in range(size):
                p.append(int(request.form['frm_key'+str(i)+str(j)]))
            key.append(p)
        while True:
            if len(pt)<=i*3:
                break
            else:
                i+=1
        temp=i

        for i in range(size):
            a=[]
            for j in range(temp):
                a.append(0)
            pt1.append(a)

        k=0
        for i in range(temp):
            for j in range(size):
                if k!=len(pt):
                    pt1[j][i]=ord(pt[k])-97
                    k+=1
                else:
                    break

        ct, ans= hill_encryption(pt1,key,size,pt)

        #return '%s %s %s' % (ct,key,ans)
        return render_template('hill_cipher_display.html',ct = ct,pt = pt, key1 = key,key=key, ans = ans,text = "Encrypted Text",size = size,suggestion = "Please Click on the text fields in order to view the Content!!\nIf you want to decrypt a text then write that text in Encrypted text field ")
@app.route('/hill_cipher_decryption',methods = ['POST','GET'])
def decryption_hill():
    if request.method == 'POST':
        ct  =  request.form['frm_pt']
        size = int(request.form['inp'])
        length = int(request.form['size'])
        ct1=[]
        key=[]
        txt=""
        for i in range(size):
            p=[]
            for j in range(size):
                p.append(int(request.form['frm_key'+str(i)+str(j)]))
            key.append(p)
        while True:
            if len(ct)<=i*3:
                break
            else:
                i+=1
        temp=i

        for i in range(size):
            a=[]
            for j in range(temp):
                a.append(0)
            ct1.append(a)

        k=0
        for i in range(temp):
            for j in range(size):
                if k!=len(ct):
                    ct1[j][i]=ord(ct[k])-97
                    k+=1
                else:
                    break

        pt=hill_decryption(ct1,key)
        for i in range(len(pt)):
            txt+=pt[i]

        return render_template('hill_cipher_display.html',ct = txt,pt = "",key1 = key, key = key,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!\nIf you want to decrypt a text then write that text in Encrypted text field ")
    else:
        return render_template('hill_cipher_display.html',ct = pt,pt = pt, key = key,text = "Decrypted Text",suggestion = "Please Click on the text fields in order to view the Content!!\nIf you want to decrypt a text then write that text in Encrypted text field ")




if __name__  ==  '__main__':
    app.run(debug='True')