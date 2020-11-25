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
				# Create a instance of SavingsAccount class 
				pass
			elif account_type == 'checquing_account':
				# Create a instance of ChecquingAccount class
				pass

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
		pass

	def search_account(self, account_number):
		"""
			return account match from list of accounts
		"""
		pass