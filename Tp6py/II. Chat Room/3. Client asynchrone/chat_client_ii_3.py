import asyncio
from aioconsole import ainput

class ChatroomClient:
    def __init__(self, host: str = "9.2.4.3", port: int = 13337):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None
        self.input_task = None
        self.receive_task = None
        asyncio.run(self.connect())

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        print("Connected to server")
        self.send("Hello")

    def send(self, message: str):
        self.writer.write(message.encode())

    async def receive(self):
        data = await self.reader.read(1024)
        return data.decode()

    def close(self):
        if self.writer:
            self.writer.close()
        print("Connection closed")

    async def user_input(self):
        try:
            while True:
                message = await ainput("Message: ")
                self.send(message)
                response = await self.receive()
                print("Server response:", response)
        except asyncio.CancelledError:
            pass

    async def async_receive(self):
        try:
            while True:
                response = await self.receive()
                print("Server response:", response)
        except asyncio.CancelledError:
            pass

    async def main(self):
        self.input_task = asyncio.create_task(self.user_input())
        self.receive_task = asyncio.create_task(self.async_receive())
        await asyncio.gather(self.input_task, self.receive_task)

if __name__ == "__main__":
    client = ChatroomClient()
    asyncio.run(client.main())
    client.close()
