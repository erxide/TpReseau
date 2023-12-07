import socket
import asyncio

class ChatroomServer :
    def __init__(self, host: str = "9.2.4.3", port : int = 13337):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket = None

    def start(self):
        asyncio.start_server(self.accept, self.host, self.port)
        self.socket.listen(5)
        print("Server started")

    def accept(self):
        self.client_socket, self.client_socket = self.socket.accept()
        print(f"Client connected {self.client_socket}")
        print(self.receive(1024))
        self.send(f"Hello {self.client_socket}")


    def send(self, message: str):
        self.client_socket.send(message.encode())

    def receive(self, bits: int = 1024):
        return self.client_socket.recv(bits).decode()
    
    def close(self):
        self.socket.close()
        print("Connection closed")

    def close_client(self):
        self.client_socket.close()
        print("Client connection closed")

if __name__ == "__main__":
    server = ChatroomServer()
    server.start()
    server.accept()
    server.close_client()
    server.close()