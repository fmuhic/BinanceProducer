import asyncio

class Consumer:
    def __init__(self):
        pass

    async def process_msg(self, formated_msgs):
        while True:
            while formated_msgs:
                msg = formated_msgs.popleft()
                await self.consume(msg)
            await asyncio.sleep(0.1)

    def get_task(self, formated_msgs):
        return asyncio.ensure_future(self.process_msg(formated_msgs))

    async def consume(self, msg):
        pprint(msg)
        await asyncio.sleep(0)
