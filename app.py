from Connection import StablishConnection
def main():
    finish = False
    while True: 
        if finish == True: 
            return 
        salida = input ("Te gustaira terminar el programa?, ingresa q para terminar")
        if salida == "q" : finish = True 
        protocol = input("Ingrese tipo de protocolo: \n>: ")
        

        connection = StablishConnection(8080, protocol)
        connection.create_server_connection()
        file_name = input("\nIngrese el archivo a enviar \n>: ")



if __name__ == '__main__':
    main()