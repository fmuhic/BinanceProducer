import asyncio
from collections import deque

class Exchange:
    def __init__(self, event_loop, producer, parser, consumer):
        self.__raw_msgs = deque()
        self.__formated_msgs = deque()
        self.event_loop = event_loop   
        self.producer = producer
        self.parser = parser
        self.consumer = consumer

    def run(self):
        fetch_tasks = self.producer.get_tasks(self.__raw_msgs)
        parse_task = self.parser.get_task(self.__raw_msgs, self.__formated_msgs)
        consume_task = self.consumer.get_task(self.__formated_msgs)
        all_tasks = asyncio.gather(*fetch_tasks, parse_task, consume_task)
        self.event_loop.run_until_complete(all_tasks)
        
        
