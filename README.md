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
buy_order = mb.fast_buy(coin='BTC', cost=5)

# Sell 0.00001 bitcoins
sell_order = mb.fast_sell(coin='BTC', qty=0.00001)

# Get informations about the orders made
buy_order_data = mb.get_orders(coin='BTC', order_id=buy_order['orderId'])
sell_order_data = mb.get_orders(coin='BTC', order_id=sell_order['orderId'])

```
