import socket
import filetype
class StablishConnection():
    
    def __init__(self, port, protocol):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = port
        self.FORMAT = "utf-8"
        self.SIZE = 1024
        self.client = None
        self.protocol = 0
        self.proto = protocol
        self.ADDR = (bytearray(),port)
        


    def get_client(self):
        if self.proto == "tcp":
            self.protocol = socket.SOCK_STREAM 
        else: 
            self.protocol = socket.SOCK_DGRAM

        try:
            self.client = socket.socket(socket.AF_INET, self.protocol)
        except socket.error as error: 
            print(f'Couldnt get connection due: {error}')

        self.ADDR= (self.IP, self.PORT)
        self.client.connect(self.ADDR)
    
    
    def send_file(self, file_name):
        BASE_PATH = "Data/"
        file_type = filetype.guess(f'{BASE_PATH}{file_name}')
        file_action='r'

        #TODO: Agregar los file_new actions segun el tipo de archivo que se esta recibiendo
        if file_type == 'image':
            file_action = "r"
        elif file_type == "video":
            file_action= "rb"

        try:
            file_send = open(f'{BASE_PATH}{file_name}', f"{file_action}")
            data = file_send.read()
            directory = f'{BASE_PATH}{file_name}'
            self.client.send(f"{directory}".encode(self.FORMAT)) 
            msg = self.client.recv(self.SIZE).decode(self.FORMAT)

            print(f'{msg}')
            file_send.close()
        except socket.error as err: 
            print("Error", err)
        

    def close_connection(self): 
        try: 
            self.client.close()
        except: 
            print("Something wrong")

    def create_server_connection(self): 

        #TODO: make the service background
        if self.proto == "tcp":
            self.protocol = socket.SOCK_STREAM 
        else: 
            self.protocol = socket.SOCK_DGRAM
        print("[EMPEZANDO] El servidor esta iniciando")
        server = socket.socket(socket.AF_INET, self.protocol)  # Se crea el servidor
        server.bind(self.ADDR)  # Se establece la conexion
        server.listen()  # Hacemos que el server este escuchando alguna peticion
        print("[ESCUCHANDO] El servidor esta en la escucha")

        while True:
            conn, addr = server.accept()  # Se establece la conexion con el cliente
            print(f"[NUEVA CONEXION] {addr} conectado.")

            filename = conn.recv(self.SIZE).decode(self.FORMAT)  # Se recibe el archivo (vacio)
            print("[RECV] Archivo recivido.")
            file_old = open(filename, "r")
            filename = filename.split(".")
            filename[0] = filename[0]+"_recv."
            filename = filename[0]+filename[1]
            file_new = open(filename, 'w')  # Abrimos el archivo (vacio)
            conn.send("Archivo recivido.".encode(self.FORMAT))

            data = conn.recv(self.SIZE).decode(self.FORMAT)  # Se recibe la data (texto)
            print(f"[RECV] Archivo de datos recibidos")
            file_new.write(file_old.read())  # Se escribe la data en el el archivo
            conn.send("Archivo de datos recivido".encode(self.FORMAT))  # Se almacena

            file_new.close()
            file_old.close()  # Cerramos el archivo
            conn.close()  # Cerramos la conexion con el cliente
            print(f"[DESCONECTADO] {addr} desconectado")

