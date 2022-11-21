# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application
import math
 
def leerr():
    archivo=open('mensajerecibido.txt','r')
    a=archivo.read()
    archivo.close()
    return a
def leere():
    archivo=open('mensajedeentrada.txt.','r')
    a=archivo.read()
    archivo.close()
    return a
def escribir(texto):
    final=texto
    archivo=open('mensajerecibido.txt','w')
    archivo.write(str(final))
    archivo.close()
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
 
 
p = 11
q = 23
n = p*q
e = 3
phi = (p-1)*(q-1)
 

#d =147
 
# Message to be encrypted
msg=1010


 
# Encryption c = (msg ^ e) % n
def en(msg,p,q):
    if(p==11 and q==23):
        
        p=p
        q=q
        n=p*q
        e=3
        c = pow(msg, e)
        c = math.fmod(c, n)
        escribir(c)
        print("crifrado")
    else:
        print("clave incorrecta")


 
# Decryption m = (c ^ d) % n
def des(d):
    if(d==147):
        c=leerr()
        print(c,"hola")
        p=11
        q=23
        n=p*q
        e=3
        d=d
        c=leerr()
        c=245.0
        e=0
        m = pow(c, d)
        m = math.fmod(m, n)
        escribir(m)
        print("cifrado")
    else:
        print("llave invalida")
        


 
 
# This code is contributed by Pranay Arora.
