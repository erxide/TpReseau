import asyncio

# Pour changer l'ip et le port du serveur, go ligne 36 bro

class ChatroomServer:
    def __init__(self, host : str = "9.2.4.3", port : int = 13337):
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer):
        client_address = writer.get_extra_info('peername')
        print(f"Client connecté: {client_address}")

        message = (await reader.read(1024)).decode()
        print(f"Message reçu du client {client_address}: {message}")

        response_message = f"Hello {client_address[0]}:{client_address[1]}"
        writer.write(response_message.encode())
        await writer.drain()

        print(f"Fermeture de la connexion avec le client {client_address}")
        writer.close()

    async def start(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port)

        address = server.sockets[0].getsockname()
        print(f"Serveur en écoute sur {address}")

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    # server = ChatroomServer("ip", port), ChatroomServer() prend les valeurs par défaut
    server = ChatroomServer()
    asyncio.run(server.start())

