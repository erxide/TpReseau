import socket

class ChatroomClient : 
    def __init__(self, host: str = "9.2.4.3", port : int = 13337):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
    def connect(self):
        self.socket.connect((self.host, self.port))
        print("Connected to server")
        self.send("Hello")

    def send(self, message: str):
        self.socket.send(message.encode())
    
    def receive(self):
        return self.socket.recv(1024).decode()
    
    def close(self):
        self.socket.close()
        print("Connection closed")

if __name__ == "__main__":
    client = ChatroomClient()
    client.connect()
    print(client.receive())
    client.close()