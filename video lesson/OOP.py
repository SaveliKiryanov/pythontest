class Account:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.__balance = balance
	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print("Пополнение прошло успешно")

	def show_balance(self):
		print(f"баланс: {self.__balance}")

#my_account = Account("Alice", 100)
#my_account.show_balance()
#y_account.deposit(1000)
#my_account.show_balance()

class CheckingAccount(Account):
	def __init__(self, owner, balance=0):
		super().__init__(owner, balance)

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print("Пополнение на рассчетный счет прошло успешно")


