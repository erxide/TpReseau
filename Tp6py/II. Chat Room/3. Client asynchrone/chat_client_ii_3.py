import asyncio
from aioconsole import ainput

class ChatroomClient:
    def __init__(self, host: str = "9.2.4.3", port: int = 13337):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(host=self.host, port=self.port)
        print("Connected to server")
        self.send("Hello")

    def send(self, message: str):
        self.writer.write(message.encode())

    async def input_loop(self):
        while True:
            user_input = await ainput("Your message: ")
            self.send(user_input)

    async def receive_loop(self):
        while True:
            data = await self.reader.read(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")

    def close(self):
        if self.writer:
            self.writer.close()
        print("Connection closed")

async def main():
    client = ChatroomClient()

    try:
        await client.connect()

        input_task = asyncio.ensure_future(client.input_loop())
        receive_task = asyncio.ensure_future(client.receive_loop())

        await asyncio.gather(input_task, receive_task)
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())
