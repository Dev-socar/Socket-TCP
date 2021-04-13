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
            self.client = socket.socket(socker.AF_INET, self.protocol)
        except socket.error as error: 
            print(f'Couldnt get connection due: {error}')

        self.ADDR= (self.IP, self.PORT)
        self.client.connect(self.ADDR)
    
    
    def send_file(self, file_name):
        BASE_PATH = "Data/"
        file_type = filetype.guess(f'{BASE_PATH}{file_name}')
        file_action=''

        #TODO: Agregar los file actions segun el tipo de archivo que se esta recibiendo
        if file_type == 'image':
            file_action = "r"
        elif file_type == "video":
            file_action= "rb"

        try:
            file = open(f'{BASE_PATH}{file_name}', f"{file_action}")
            data = file.read(ecs)
            self.client.send(f"{file_name}".encode(self.FORMAT)) 
            msg = self.client.receive(self.SIZE).decode(self.FORMAT)
            print(f'{SERVER} :{msg}')
            file.close()
        except: 
            print("Error")

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
            file = open(filename, 'r')  # Abrimos el archivo (vacio)
            conn.send("Archivo recivido.".encode(self.FORMAT))

            data = conn.recv(self.SIZE).decode(self.FORMAT)  # Se recibe la data (texto)
            print(f"[RECV] Archivo de datos recibidos")
            file.write(data)  # Se escribe la data en el el archivo
            conn.send("Archivo de datos recivido".encode(FORMAT))  # Se almacena

            file.close()  # Cerramos el archivo
            conn.close()  # Cerramos la conexion con el cliente
            print(f"[DESCONECTADO] {addr} desconectado")

