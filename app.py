from Connection import StablishConnection
def main():
    finish = False
    while True: 
        if finish == True: 
            return 

        protocol = input("Ingrese tipo de protocolo: \n>: ")
        connection = StablishConnection(8080, protocol)
        connection.create_server_connection()
        file_name = input("\nIngrese el archivo a enviar \n>: ")
        
if __name__ == '__main__':
    main()