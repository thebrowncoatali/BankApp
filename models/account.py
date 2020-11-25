from models.transaction import Transaction


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

	def deposit(self, amount):
		"""
			this funtion take amount as
			parameter log the transaction and does a deposit
		"""
		# Create Transation
		transaction = Transaction(type_transaction='deposit', amount=amount)
		self._transactions.append(transaction)

		#also we can apply bank interest
		self._current_balance+=amount


class SavingsAccount(Account):
	"""
		Inherit form Account class.
		this class is a specific account type:

		Saving Account:

		additional parameter ==> minimum_balance
	"""

	def __init__(self, **kwargs):
		self._minimum_balance = kwargs.pop('minimum_balance')
		super().__init__(**kwargs)

	def get_minimum_balance(self):
		"""
			return minimum balance
		"""
		return self._minimum_balance

	def withdraw(self, amount):
		"""
			These accounts require account holders to maintain 
			a minimum balance in the account. 
			E.g. if the minimum balance is 5000 CAD and
			the current balance in the account is 7000 CAD, 
			the maximum withdrawal that can be allowed is 2000 CAD
		"""
		pass


class ChecquingAccount(Account):
	"""
		Inherit form Account class.
		this class is a specific account type:

		Checquing Account:

		additional parameter ==> overdraft_allowed
	"""

	def __init__(self, **kwargs):
		self._overdraft_allowed = kwargs.pop('overdraft_allowed')
		super().__init__(**kwargs)

	def get_overdraft_allowed(self):
		"""
			return overdraft allowed
		"""
		return self._overdraft_allowed

	def withdraw(self, amount):
		"""
			These accounts allow overdrafts. 
			This means if an account has an overdraft limit of 5000 CAD, 
			the account holder is allowed to withdraw up to 5000 CAD 
			more than the money they have in the account.
		"""
		pass

