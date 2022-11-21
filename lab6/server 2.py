
# # DOCUMENTACIÓN
# Establecimiento de conexión servidor/cliente
# ¬https://www.youtube.com/watch?v=-ve1ZtDrUCo
# Establecimiento de encriptacion DES
# ¬https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
#Codigo adaptado para las necesidades del problema
#from Crypto.Cipher import DES
import socket
from R_S_A import des
from R_S_A import en
cont=1


def leer():
    archivo=open('mensajerecibido.txt','rb')
    a=archivo.read()
    archivo.close()
    return a

b=input('Ingrese b hellman 5 ')
e=input('ingrese llave privada Q 23')

#modulo 23
socket_ser=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_ser.bind(('localhost',8585))
socket_ser.listen()
print('El server ta ready')
print('se iniciaran los protocolos de sincronizacion con el cliente, por favor sigua las intrucciones')
while True:
    socketconexion,add=socket_ser.accept()
    print('se conecto ', add)

    while True:
        mensaje_recibido=socketconexion.recv(1024).decode()
    
        if 'clave ' in mensaje_recibido:
            P=mensaje_recibido.strip('clave ')
            print('credenciales recividas')
            print('aprete enter')
            P=P.split(' ')
            
            A=int(P[0])
            Q=int(P[1])
            print(A,Q)
            

            K=(A**5)%(35)
            if(K==11):
                socketconexion.send(('aceptado').encode())
            else:
                socketconexion.send(('N').encode())
                
        elif 'c' in mensaje_recibido:
            
            
            if(K==11):
                en(1010,K,Q)
                socketconexion.send(('cifrado').encode())
            
        elif 'd'in mensaje_recibido:
            socketconexion.send(('in').encode())
            
            
        elif '147' in mensaje_recibido:
            des(147)
    
        elif mensaje_recibido=='-cerrar-':
            break
        else:
            if 'Enviar texto codificado' in mensaje_recibido:
                print('')
            elif cont==1:
                print('ya esta listo, Escriba "se esta viendo"')
                cont+=1
            else:
                print('--->',mensaje_recibido)
        socketconexion.send(input().encode())
        
    print('se desconecto la conexion con: ',add)
    socketconexion.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
