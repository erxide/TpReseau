import socket
import asyncio

def handle_client(client_socket):
    print(f"Client connected {client_socket}")
    message = receive(client_socket, 1024)
    print(message)
    send(client_socket, f"Hello {client_socket}")
    close_client(client_socket)

def send(client_socket, message):
    client_socket.send(message.encode())

def receive(client_socket, bits=1024):
    return client_socket.recv(bits).decode()

def close_client(client_socket):
    client_socket.close()
    print("Client connection closed")

async def start_server(host="9.2.4.3", port=13337):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server started")

    while True:
        client_socket, _ = server.accept()
        asyncio.create_task(handle_client(client_socket))

if __name__ == "__main__":
    asyncio.run(start_server())
