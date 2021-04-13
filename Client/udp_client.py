import socket
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'Connection.py')))
from Connection import StablishConnection

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def UDPClient():
    """
        1. Crear cliente. 
        2. Establecemos conexion con server
        3. Enviamos paquete 
        4. Cerramos file y cliente
    
    """
    cliente  = 



    


