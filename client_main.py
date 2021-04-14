from Connection import StablishConnection

def main():

    try:
        file_name = input("Ingresa el nombre del archivo que vas a enviar: \n>:")
        tipo = input("Ingresa el tipo de cliente (tcp/udp): \n>:")
    except:
        print("Error al tratar de optener los datos")

    try: 
        cli = StablishConnection(8080, tipo)
        cli.get_client()
        cli.send_file(file_name)
        cli.close_connection()
    except:
        print("Ocurrio un error al mandar tu archivo")

if __name__ == "__main__":
    main()