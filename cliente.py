import serial
import time
import socket, sys
s=socket.socket()
s.connect(('localhost', 1002))
s.send("Hola soy el cliente")
respuesta=s.recv(1024)
print respuesta
a=input()
while True:
    if a is "adios":
        s.close()

