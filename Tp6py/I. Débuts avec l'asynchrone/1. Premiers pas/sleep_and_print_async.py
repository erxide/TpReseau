import asyncio

async def func():
    for i  in range(10):
        print(i + 1)
        await asyncio.sleep(0.5)

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(func()), 
    loop.create_task(func())
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()