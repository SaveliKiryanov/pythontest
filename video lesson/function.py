transactions =[100,50,-200,550]

def apply_transactions(transactions):
	balance = 0
	for transaction in transactions:
		if transaction > 0:
			print(f"Пополнение на сумму {transaction}")
		else:
			print(f"Снятие на сумму {transaction}")
		balance += transaction
	print(f"Финальный баланс {balance}")

#apply_transactions(transactions)

def reach_min_balance(initial_balance, min_balance):
	while initial_balance < min_balance:
		print(f"Текущий баланс {initial_balance} меньше минимальной суммы. Добавляем депозит 100")
		initial_balance += 100
	print(f"Достигнут минимальный баланс {min_balance}")

#reach_min_balance(50, 300)

def check_trasactions(transaction):
	if transaction > 0:
		print("Депозит")
	elif transaction < 0:
		print("Списание")
	else:
		print("Транзакция не меняет баланс")

#check_trasactions(100)
#check_trasactions(-20)
#check_trasactions(0)

account_actions = {"initial_value": 100, "withdraw_1": -50, "deposit_2": 50 }
def print_actions_names(accont_actions):
	for action, value in account_actions.items():
		print(f"Действия: {action}, значения {value}")

#print_actions_names(account_actions)

def safe_withdraw(balance, amount):
	try:
		if amount > balance:
			raise ValueError("Сумма снятия больше доступного баланса")
		balance -= amount
		print(f"Снятие произошло успешно, оставшийся баланс {balance}")
	except ValueError as error:
		print(error)
safe_withdraw(100, 150) 		