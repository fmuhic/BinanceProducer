import asyncio
import requests
import json
import re

from exchanges.exchange_base import Exchange
from producers.base_producer import WebsocketProducer
from parsers.base_parser import Parser
from consumers.base_consumer import Consumer
from pprint import pprint

# Todo(Fudo):
# - Error handling
# - Docstrings
# - Command line arguments (argparse)
# - Logger
# - Partial symbol producer
# - Docker support

class BinanceParser(Parser):
    def format_msg(self, msg, symbol):
        return {
                'exchange'   : 'BINANCE',
                'event'      : 'TRADE',
                'symbol'     : symbol,
                'price'      : float(msg['p']),
                'quantity'   : float(msg['q']),
                'taker_side' : 'BUY' if msg['m'] else 'SELL',
                'timestamp'  : float(msg['E']) / 1000.0
               }


class BinanceConsumer(Consumer):
    # If you wish to store messages to db, provide async db controller here!
    #  def __init__(self, db):
        #  self.db = db

    async def consume(self, msg):
        #  await self.db.store(msg)
        pprint(msg)
        await asyncio.sleep(0)


class BinanceMetadata():
    def __init__(self, ws_endpoint, symbol_endpoint):
        self.ws_endpoint = ws_endpoint
        self.symbol_endpoint = symbol_endpoint
    
    def get_ws_info(self):
        symbols = self.__get_symbols()
        return [{'endpoint': self.ws_endpoint % symbol_id,
                 'symbol': symbol_name} for symbol_id, symbol_name in symbols]
    
    def __get_symbols(self):
        resp = requests.get(self.symbol_endpoint)
        exchange_metadata = json.loads(resp.text)
        symbols = []
        for s in exchange_metadata['symbols']:
            symbol_name = s['baseAsset'] + '_' + re.sub(s['baseAsset'], '', s['symbol'])
            symbol_id = s['symbol'].lower()
            symbols.append([symbol_id, symbol_name])
        return symbols


if __name__ == '__main__':
    metadata = BinanceMetadata(ws_endpoint='wss://stream.binance.com:9443/ws/%s@trade',
                               symbol_endpoint='https://api.binance.com/api/v1/exchangeInfo')
    collector = WebsocketProducer(metadata.get_ws_info())
    parser = BinanceParser()
    consumer = BinanceConsumer()
    loop = asyncio.get_event_loop()
    ex = Exchange(loop, collector, parser, consumer)
    ex.run()
