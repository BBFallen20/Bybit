import asyncio
import websockets


connected = set()


async def serv(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            for connection in connected:
                if connection != websocket:
                    await connection.send(f'Your message: {message}')
    finally:
        connected.remove(websocket)


server = websockets.serve(serv, 'localhost', 6000)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
