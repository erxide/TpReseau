import socket

def handle_client(client_socket):
    client_address = client_socket.getpeername()
    print(f"Client connecté: {client_address}")

    data = client_socket.recv(1024)
    message = data.decode()
    print(f"Message reçu du client {client_address}: {message}")

    response_message = f"Hello {client_address[0]}:{client_address[1]}"
    client_socket.send(response_message.encode())

    print(f"Fermeture de la connexion avec le client {client_address}")
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 8888)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print(f"Serveur en écoute sur {server_address}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            handle_client(client_socket)

    except KeyboardInterrupt:
        print("Arrêt du serveur.")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
