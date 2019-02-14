# Binance exchange trade producer

This application fetches all trade data for all available crypto symbols from Binance.

# Installation

- Make sure you have python 3.5 or newer.
- Create virtual environment and install required packages:
```
 $ virtualenv venv
 $ . venv/bin/activate
 $ pip install websockets
 $ pip install requests
```
- Run producer:
```
 $ python3.7 main.py
```

# Output example
```
...
{'event': 'TRADE',
 'exchange': 'BINANCE',
 'price': 0.01157,
 'quantity': 0.17,
 'symbol': 'LTC_BTC',
 'taker_side': 'SELL',
 'timestamp': 1550181445.579
}
{'event': 'TRADE',
 'exchange': 'BINANCE',
 'price': 3600.79,
 'quantity': 0.003327,
 'symbol': 'BTC_USDT',
 'taker_side': 'BUY',
 'timestamp': 1550181445.734
}
{'event': 'TRADE',
 'exchange': 'BINANCE',
 'price': 0.071813,
 'quantity': 0.26,
 'symbol': 'BNB_ETH',
 'taker_side': 'BUY',
 'timestamp': 1550181446.572
}
...
```

## Todo
- Documentation
- Command line arguments
- Debug mode (logging)
- Partial symbol support (only ETH_BTC and ETH_USDT for example)
- Docker support
