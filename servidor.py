import serial
import time
from socket import socket

s = socket.socket()
s.bind ( ('64.76.142.170', 1002) )
s.listen(10)

while True:
    conexion, direccion=s.accept()
    print "conexion establecida"
    arduino=serial.Serial('COM3',9600)#CMO4 es el canal donde esta conectado el arduino
    time.sleep(2)
    rawString=arduino.readline()
    conexion.send(rawString)
    arduino.close()
    conexion.close()
