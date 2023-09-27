#ipc.py
import json
import time
import asyncio
import websockets

from utils.utils import json_serial

class IPCClient:
    def __init__(self, port):
        self.uri = f"ws://localhost:{port}"
        self.ready = False
        self.websocket = None

    async def connect(self):
        async with websockets.connect(self.uri) as websocket:
            print("Connecting to the external process...")
            self.websocket = websocket
            print("Connected!")

    async def listen(self):
        if not self.websocket:
            print("Not connected to the external process!")
            return

        async for data in self.websocket:
            message = json.loads(data)
            if message['type'] == 'response':
                return message['content']

    async def send(self, data):
        if not self.websocket:
            print("Not connected to the external process!")
            return

        serialized_data = json.dumps(data, default=json_serial)
        await self.websocket.send(serialized_data)
        print(serialized_data)