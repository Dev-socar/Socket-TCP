class stablish_connection():
    
    def __init__(self, port):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = port
        self.FORMAT = "utf-8"
        self.SIZE = 1024


    def transfer_data_udp(file_path):
        ADDR= (IP, PORT)
        client = socket.socket(socker.AF_INET, socket.SOKC_STREAM)
        client.connect(self.ADDR)
        file = open(f'{file_path}', "r")
        data = file.read()
        
        client.send("file.txt".encode(FORMAT)) 
        msg = client.receive(self.SIZE).decode(FORMAT)
        print(f'{SERVER} :{msg}')

        file.close()
        client.close()
    
    def tansfer_data_tcp(file_path):
