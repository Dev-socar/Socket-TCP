import socket

IP = socket.gethostbyname(socket.gethostname())  # HOST
PORT = 8080  # El puerto de la conexion
ADDR = (IP, PORT)  # Direecion
FORMAT = "utf-8"  # Formato para codificar y descodificar el file
SIZE = 1024  # Tamaño del archivo


def Server():
    print("[EMPEZANDO] El servidor esta iniciando")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Se crea el socket
    server.bind(ADDR)  # Se establece la conexion
    server.listen()  # Hacemos que el server este escuchando alguna peticion
    print("[ESCUCHANDO] El servidor esta en la escucha")

    while True:
        conn, addr = server.accept()  # Se establece la conexion con el cliente
        print(f"[NUEVA CONEXION] {addr} conectado.")

        filename = conn.recv(SIZE).decode(
            FORMAT)  # Se recibe el archivo (vacio)
        print("[RECV] Archivo recivido.")
        file = open(filename, "w")  # Abrimos el archivo (vacio)
        conn.send("Archivo recivido.".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)  # Se recibe la data (texto)
        print(f"[RECV] Archivo de datos recibidos")
        file.write(data)  # Se escribe la data en el el archivo
        conn.send("Archivo de datos recivido".encode(FORMAT))  # Se almacena

        file.close()  # Cerramos el archivo
        conn.close()  # Cerramos la conexion con el cliente
        print(f"[DESCONECTADO] {addr} desconectado")
        


if __name__ == "__main__":
    main()
