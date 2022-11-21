
# # DOCUMENTACIÓN
# Establecimiento de conexión servidor/cliente
# ¬https://www.youtube.com/watch?v=-ve1ZtDrUCo
# Establecimiento de encriptacion DES
# ¬https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
#Codigo adaptado para las necesidades del problema

import socket
import sys
#from Crypto.Cipher import DES
def leer():
    archivo=open('mensajedeentrada.txt.','r')
    a=archivo.read()
    
    archivo.close()
    return a
def escribir(texto):
    final=texto
    archivo=open('mensajerecibido.txt','wb')
    archivo.write(final)
    archivo.close()

key=B'12345678'

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

print("sincronizando, por favor ingresar parametros sig \n")
P=(input('Ingrese la clave  A para sinvronizacion de llave 10->'))
#G=(input('Ingrese la ckave G que es publica y esta entre 0 y P : '))
#a=(input(('Ingrese su llave privada que esta1 entre 0 y P-1: ')))
print('se iniciaran los protocolos de sincronizacion con el servidor, por favor sigua las intrucciones')
#print('Para poder enviar un el texto codificado, debe escribir "Enviar texto codificado" ')

socket_cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_cli.connect(('localhost',8585))
uno=True
print('Esperando conexion')
while True: 
    if uno==1:
        socket_cli.send(('clave' + " "+P).encode())
        uno=False
    mensaje=input()
    if mensaje!='-cerrar-':
        socket_cli.send(mensaje.encode())
        respuesta=socket_cli.recv(1024).decode()

        if 'aceptado' in respuesta:
            preguntar=input('Conexion establecida, elija accion\n Cifrar=c \n Decifrar=d\n')
            if(preguntar=='c' or preguntar=='C'):
                socket_cli.send(('c').encode())
            elif(preguntar=='d' or preguntar=='D'):
                socket_cli.send(('d').encode())

            #print('Escriba "mandar ka"')
            #B=respuesta.strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
            #ka = int(pow(int(B),int(a),int(P)))
        if 'cifrado' in respuesta:
            print('cifrado correcto')
        if mensaje=='mandar ka':
            mensaje='Esta es ka '+str(ka)
            print('presione enter')
            socket_cli.send(mensaje.encode())
        if respuesta=='se esta viendo':
            print('escriba cualquier cosa para continuar, Para enviar archivo cifrado debe escribir "Enviar texto codificado"')
        if mensaje=='Enviar texto codificado':
            mensaje=leer()
            mensaje=mensaje.encode()
            padded_text = pad(mensaje)
            des = DES.new(key, DES.MODE_ECB)
            encrypted_text = des.encrypt(padded_text)
            #escribir(encrypted_text)
            # de6s 1
            des1= DES.new(key, DES.MODE_ECB)
            encrypted_text1= des1.encrypt(encrypted_text)
            #escribir(encrypted_text)
            #des2
            des2= DES.new(key, DES.MODE_ECB)
            encrypted_text2 = des2.encrypt(encrypted_text1)
            #escribir(encrypted_text)
            #des3
            des3= DES.new(key, DES.MODE_ECB)
            encrypted_text3 = des3.encrypt(encrypted_text2)
            escribir(encrypted_text3)
            
            socket_cli.send('se ha mandado un mensaje codificado, revisa'.encode())

    else:
        socket_cli.send(mensaje.encode())
        socket_cli.close()
        sys.exit()
    
