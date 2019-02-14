import asyncio
import json

class Parser:
    def __init__(self):
        pass

    def decrypt_msg(self, msg):
        return json.loads(msg)

    def get_task(self, raw_msgs, formated_msgs):
        return asyncio.ensure_future(self.parse(raw_msgs, formated_msgs))

    async def parse(self, raw_msgs, formated_msgs):
        while True:
            while raw_msgs:
                raw_msg, symbol = raw_msgs.popleft()
                decrypted_msg = self.decrypt_msg(raw_msg)
                msg = self.format_msg(decrypted_msg, symbol)
                formated_msgs.append(msg)
                await asyncio.sleep(0)
            await asyncio.sleep(0.1)

    def format_msg(self, msg, symbol):
        return msg
        
