import asyncio
import websockets


async def connection():
    url = 'ws://localhost:6000'
    async with websockets.connect(url) as websocket:
        message = input("")
        await websocket.send(message)
        await websocket.recv()


asyncio.get_event_loop().run_until_complete(connection())


