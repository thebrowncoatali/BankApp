

class Program():

	def __init__(self):
		pass

	def run(self):
		"""
			Function initializer
		"""
		self.show_main_menu()

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



		if choice == 2:
			# show second menu by the momment
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
			pass

		elif choice == 5:
			# Go back to Banking Main Menu
			self.show_main_menu()
