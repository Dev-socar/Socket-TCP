from Connection import StablishConnection

def main():
    # Creacion de un objeto de tipo servidor, que estara a la escucha 
    # de las diferentes peticiones, de los diferentes clientes

    try:
        tipo = input("Ingresa el tipo de servidor que deseas activar (tcp/udp): \n>:")
    except:
        print("Error al ingresar el tipo de servidor")
        
    serv = StablishConnection(8080, tipo)
    serv.create_server_connection()
    


if __name__ == "__main__":
    main()