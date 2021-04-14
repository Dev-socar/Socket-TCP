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
        if file_type == "image" or file_type == "video" or file_type == "audio":
            file_action = "rb"

            while True:
                file_send = open(f'{BASE_PATH}{file_name}', f"{file_action}")
                content = file_send.read(self.SIZE)
                while content:
                    self.client.send(content)
                    content = file_send.read(self.SIZE)
                break
            try:
                self.client.send("1")
            except TypeError:
                self.client.send("1".encode(self.FORMAT))
            
            file_send.close()
        else: 
            file_action = 'r'
        
        try:
            file_send = open(f'{BASE_PATH}{file_name}', f"{file_action}")
            data = file_send.read()
            directory = f'{BASE_PATH}{file_name}'
            self.client.send(f"{directory}".encode(self.FORMAT)) 
            msg = self.client.recv(self.SIZE).decode(self.FORMAT)
            self.client.send(data.encode(self.FORMAT))
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
            filename = filename.split(".")
            filename[0] = filename[0]+"_recv."
            filename = filename[0]+filename[1]
            file_new = open(filename, 'w')  # Abrimos el archivo (vacio)
            conn.send("Archivo recivido.".encode(self.FORMAT))

            data = conn.recv(self.SIZE).decode(self.FORMAT)  # Se recibe la data (texto)
            print(f"[RECV] Archivo de datos recibidos")
            file_new.write(data)  # Se escribe la data en el el archivo
            conn.send("Archivo de datos recivido".encode(self.FORMAT))  # Se almacena

            file_new.close()  # Cerramos el archivo
            conn.close()  # Cerramos la conexion con el cliente
            print(f"[DESCONECTADO] {addr} desconectado")

