

class Account():
	"""
		Account class
	"""

	# list of transactions (track all transactions)
	_transactions = []

	def __init__(self, **kwargs):
		self._account_number = kwargs.pop('account_number')
		self._account_type = kwargs.pop('account_type')
		self._account_holder_name = kwargs.pop('account_holder_name')
		self._rate_of_interest = kwargs.pop('rate_of_interest')
		self._current_balance = kwargs.pop('current_balance')

	def get_account_number(self):
		"""
			return account numnber
		"""
		return self._account_number

	def get_account_type(self):
		"""
			return account type
		"""
		return self._account_type

	def get_account_holder_name(self):
		"""
			return account holder name
		"""
		return self._account_holder_name

	def get_rate_of_interest(self):
		"""
			return rate of interest
		"""
		return self._rate_of_interest

	def get_current_balance(self):
		"""
			return current balance
		"""
		return self._current_balance



