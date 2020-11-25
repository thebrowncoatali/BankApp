

class Transaction():
	"""
		Transaction Class:
	"""

	def __init__(self, type_transaction, amount):
		self._type = type_transaction
		self._amount = amount

	def get_transaction_type(self):
		"""
			return transaction type
		"""
		return self._type

	def get_transaction_amount(self):
		"""
			return transaction amount
		"""
		return self._amount