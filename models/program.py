from models.bank import Bank


class Program():
	current_account = None

	def __init__(self):
		self.bank = Bank('Bank of Canada')

	def run(self):
		"""
			Function initializer
		"""
		self.show_main_menu()

	def _get_current_account(self):
		"""
			this function ask for account number 
			and search match in accounts data.

			return account match
		"""
		account_to_search = input('Enter the account number: ')
		account_match = self.bank.search_account(account_to_search)
		return account_match

	def show_main_menu(self):
		"""
			Display the Banking Main Menu

				** Open Account
				** Select Account
				** Exit
		"""
		print(
			'',
			'===================',
			'Backing Main Menu:',
			'===================',
			' ** Open Account [1]',
			' ** Select Account [2]',
			' ** Exit [3]', 
			sep='\n'
		)

		choice = None
		while not choice:
			# Ask user choice
			choice = input('Please choice an option: ')

			# Validate choice

			# First validation:
			try:
				choice = int(choice)
			except:
				return None

			# Second Validation
			if choice > 3 or choice < 1:
				choice = None

			# Error message
			if not choice:
				print('\nInvalid choice, please try again. choice a number between [1-3]')

		if choice == 1:
			# Create a new account
			# ask details to the user
			new_account = {}
			new_account['account_holder_name'] = input('Enter account holder name: ')

			print(
				'Account types:',
				' ** Saving Account [1]',
				' ** Checquing Account [2]',
				sep='\n'
			)

			choice = None
			while not choice:
				# Ask user choice
				choice = input('Please choice an option: ')

				# Validate choice

				# First validation:
				try:
					choice = int(choice)
				except:
					return None

				# Second Validation
				if choice > 2 or choice < 1:
					choice = None

				# Error message
				if not choice:
					print('\nInvalid choice, please try again. choice a number between [1-2]')

			if choice == 1:
				# set as saving account
				new_account['account_type'] = 'saving_account'
			else:
				# set as checquing account
				new_account['account_type'] = 'checquing_account'

			# create a new account
			account_created = self.bank.open_account(**new_account)
			# successfully message
			print('\nUser was created successfully')
			print(
				'================================',
				'===== New Account Details ======',
				'** Bank number: {}'.format(account_created.get_account_number()),
				'** Holder Name: {}'.format(account_created.get_account_holder_name()),
				'================================',
				sep='\n'
			)			# go to main menu
			self.show_main_menu()


		if choice == 2:
			# seach by account number
			while not self.current_account:
				self.current_account = self._get_current_account()
				if not self.current_account:
					print('Please, account number not registered. Please try again.')

			# show account menu
			self.show_account_menu()


		elif choice == 3:
			# Exit the program
			exit()		



	def show_account_menu(self):
		"""
			Display the Account Menu

				** Check Balance
				** Deposit
				** Withdraw
				** Display Transactions
				** Exit Account: go back to Banking Main Menu
		"""
		print(
			'\n=====================',
			'Account Menu:',
			'=====================',
			' ** Check Balance [1]',
			' ** Deposit [2]',
			' ** Withdraw [3]',
			' ** Display Transactions [4]',
			' ** Exit Account [5]', 
			sep='\n'
		)

		choice = None
		while not choice:
			# Ask user choice
			choice = input('Please choice an option: ')

			# Validate choice

			# First validation:
			try:
				choice = int(choice)
			except:
				return None

			# Second Validation
			if choice > 5 or choice < 1:
				choice = None

			# Error message
			if not choice:
				print('\nInvalid choice, please try again. choice a number between [1-5]')

		if choice == 1:
			# Logic to check balance
			print(
				'',
				'==========================',
				'Current Balance: {} CAD'.format(self.current_account.get_current_balance()),
				'==========================',
				sep='\n'
			)
			# Display Account Menu Again
			self.show_account_menu()

		elif choice == 2:
			# Logic to deposit
			amount = None
			while not amount:
				try:
					amount = float(input('Amount to deposit: '))
					if not amount >=0:
						print('Enter value greater than 0')
						amount = None
				except:
					print('Invalid value, try again')

			# Make deposit
			self.current_account.deposit(amount)

			# Display Account Menu Again
			self.show_account_menu()

		elif choice == 3:
			# Logic to withdraw
			amount = None
			while not amount:
				try:
					amount = float(input('Amount to withdraw: '))
					is_done = self.current_account.withdraw(amount)
					if not amount >=0:
						print('Enter value greater than 0')
						amount = None
				except:
					print('Invalid value, try again')
			
			#Check if was made sussccefully
			if not is_done:
				if self.current_account.get_account_type() == 'saving_account':
					print(
						'\nError Message: This accounts require account holders to maintain',
						'a minimum balance of {} CAD'.format(self.current_account.get_minimum_balance()),
						'you do not have sufficient funds to do this operation.',
						sep='\n'
					)
				elif self.current_account.get_account_type() == 'checquing_account':
					print(
						'\nError Message: Account has an overdraft',
						'limit of {} CAD'.format(self.current_account.get_overdraft_allowed()),
						'You are getting over the overdraft.',
						sep='\n'
					)

			# Display Account Menu Again
			self.show_account_menu()

		elif choice == 4:
			# Logic display transactions
			transactions = self.current_account.get_transactions()
			if not transactions:
				print(
					'',
					'==================================',
					'You dont have transactions for now',
					'==================================',
					sep='\n'
				)
			for transaction in transactions:
				print(
					'=========================================================',
					'Transactions ======== type: {} ======== Amount: {} CAD'.format(
						transaction.get_transaction_type(),
						transaction.get_transaction_amount()
					),
					'=========================================================',
					sep='\n'
					)

			# Display Account Menu Again
			self.show_account_menu()

		elif choice == 5:
			# Go back to Banking Main Menu
			self.show_main_menu()
