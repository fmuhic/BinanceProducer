import asyncio
import websockets

class WebsocketProducer:
    def __init__(self, ws_info):
        self.ws_info = ws_info

    async def fetch(self, ws_info, raw_msgs):
        while True:
            async with websockets.connect(ws_info['endpoint']) as ws:
                resp = await ws.recv()
                raw_msgs.append([resp, ws_info['symbol']])

    def get_tasks(self, raw_msgs):
        tasks = []
        for info in self.ws_info:
            tasks.append(asyncio.ensure_future(self.fetch(info, raw_msgs)))
        return tasks
