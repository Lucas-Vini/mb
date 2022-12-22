# mb
mb is a easy-to-use client library to the mercado bitcoin APIs

## Quick start
```python

from mb import mbtrade
from mb import mbdata


mb = mbtrade.Client('your_token_id', 'your_token_secret')

# Get Bitcoin current price
last_buy_price, last_sell_price = mbdata.get_coin_last_trades_prices('BTC')

# Buy 5 reais in bitcoins
order = mb.fast_buy(coin='BTC', cost=5)

# Sell 0.00001 bitcoins
order = mb.fast_sell(coin='BTC', qty=0.00001)'''
