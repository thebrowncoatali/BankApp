from .account import SavingsAccount, ChecquingAccount
from data import ACCOUNTS

class Bank():
	"""
		Bank Class
	"""

	# to save all accounts
	_accounts_list = []

	def __init__(self, name):
		# set bank name
		self._name = name

		# list that holds the accounts objects
		for account_data in ACCOUNTS:
			# choice a class depend of account type
			account_type = account_data['account_type']
			if account_type == 'saving_account':
				# Create an instance of SavingsAccount class 
				account = SavingsAccount(**account_data)
			elif account_type == 'checquing_account':
				# Create an instance of ChecquingAccount class
				account = ChecquingAccount(**account_data)

			# add to list of accounts
			self._accounts_list.append(account)

	def get_bank_name(self):
		"""
			return bank name
		"""
		return self._name

	def open_account(self, **kwargs):
		"""
			this function create a new bank
			account:

			parameter required: 
				* account type
				* account holder name

			I think that another parameters must be set by 
			bank as: account number, rate of interest...
		"""

		# set by bank
		kwargs['rate_of_interest'] = 0.10 # set by bank
		kwargs['current_balance'] = 0 # new account
		kwargs['account_number'] =  '2142324234124' # must be a random number

		overdraft_allowed = 5000 # set by bank
		minimum_balance = 3000 # set by bank

		account_type = kwargs['account_type']
		if account_type == 'saving_account':
			# Create an instance of SavingsAccount class
			kwargs['minimum_balance'] = minimum_balance
			account = SavingsAccount(**kwargs)
		elif account_type == 'checquing_account':
			# Create an instance of ChecquingAccount class
			kwargs['overdraft_allowed'] = overdraft_allowed
			account = ChecquingAccount(**kwargs)
		
		# add new account to list of accounts
		self._accounts_list.append(account)


	def search_account(self, account_number):
		"""
			return account match from list of accounts
		"""
		for account in self._accounts_list:
			if account_number == account.get_account_number():
				return account

		return []