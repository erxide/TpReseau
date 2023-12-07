import socket

class ChatroomServer:
    def __init__(self, host="9.2.4.3", port=13337):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None
        self.client_port = None

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server started")

        while True:
            self.accept()

    def accept(self):
        client_socket, _ = self.server_socket.accept()
        print(f"Client connected {client_socket}")
        self.client_socket = client_socket

        message = self.receive(1024)
        print(message)

        self.client_address, self.client_port = self.client_socket.getpeername()

        self.send(f"Hello {self.client_socket}")


    def send(self, message):
        self.client_socket.send(message.encode())

    def receive(self, bits=1024):
        return self.client_socket.recv(bits).decode()

    def close_client(self):
        self.client_socket.close()
        print("Client connection closed")

    def close(self):
        self.server_socket.close()
        print("Server closed")


if __name__ == "__main__":
    server = ChatroomServer()
    server.start()
    server.close()
