import asyncio
import aioconsole

class ChatroomClient : 
    def __init__(self, host: str = "9.2.4.3", port : int = 13337):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None
        
    def connect(self):
        self.reader, self.writer = asyncio.open_connection(self.host, self.port)
        print("Connected to server")
        self.send("Hello")

    async def send(self, message: str):
        self.writer.write(message.encode())
        await self.writer.drain()

    async def receive(self):
        return await self.reader.read(1024)
    
    def close(self):
        self.socket.close()
        print("Connection closed")

    async def input(self):
        while True:
            input_user = await aioconsole.ainput("Message : ")
            await self.send(input_user)

    async def async_receive(self):
        while True:
            print((await self.receive()).decode())


    async def main(self):
        client = ChatroomClient()
        client.connect()
        print(client.receive())
        await asyncio.gather(client.input(), client.async_receive())
        client.close()


if __name__ == "__main__":
    client = ChatroomClient()
    asyncio.run(client.main())