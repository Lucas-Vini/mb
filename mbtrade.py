import requests

class Client():
	def __init__(self, token_id, token_secret):
		self.__token_id = token_id
		self.__token_secret = token_secret
		self.__access_token = self.__get_access_token(self.__token_id,
													  self.__token_secret)
	
	def __get_access_token(self, token_id, token_secret):
		url = 'https://api.mercadobitcoin.net/api/v4/authorize'
		data = {"login": token_id, "password": token_secret}
		access_token = requests.post(url=url, data=data).json()['access_token']
		return access_token

	def list_accounts(self):
		url = 'https://api.mercadobitcoin.net/api/v4/accounts'
		header = {"Authorization": self.__access_token}
		accounts = requests.get(url=url, headers=header)
		return accounts.json()

	def place_order(self, coin, async_order=None, cost=None, external_id=None, limit_price=None,
					qty=None, side=None, stop_price=None, order_type=None, account_id=None):

		if account_id is None:
			account_id = self.__token_id

		url = 'https://api.mercadobitcoin.net/api/v4/accounts/'
		url += '{}/{}-BRL/orders'.format(account_id, coin.upper())

		header = {"Authorization": self.__access_token}		
		data = {
				"cost": cost,
				"qty": qty,
				"side": side,
				"type": order_type
				}

		order = requests.post(url=url, headers=header, data=data)
		return order.json()

	def fast_buy(self, coin, cost):
		return self.place_order(coin=coin, cost=cost, side='buy', order_type='market')

	def fast_sell(self, coin, qty):
		return self.place_order(coin=coin, qty=qty, side='sell', order_type='market')

	def get_orders(self, coin, order_id, account_id=None):

		if account_id is None:
			account_id = self.__token_id

		url = 'https://api.mercadobitcoin.net/api/v4/accounts/'
		url += '{}/{}-BRL/orders/{}'.format(account_id, coin.upper(), order_id)

		header = {"Authorization": self.__access_token}

		order = requests.get(url=url, headers=header)
		return order.json()