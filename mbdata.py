import time
import requests

def get_coin_last_trades_prices(coin):
	now = int(time.time())
	twenty_five_mins_ago = now - 1500

	url = 'https://api.mercadobitcoin.net/api/v4/{}-BRL/trades'.format(coin)
	params = {'from': twenty_five_mins_ago, 'to': now}

	prices = requests.get(url=url, params=params)

	for price in prices.json():
		if price['type'] == 'buy':
			buy_price = price['price']
		
		if price['type'] == 'sell':
			sell_price = price['price']

	return buy_price, sell_price