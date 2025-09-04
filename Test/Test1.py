transactions = [100, -50, 200, -100]

def apply_transactions(transactions):
    balance = 0  # Начальный баланс
    for transaction in transactions:
        if transaction > 0:
            print(f"Применение депозита: {transaction}")
        else:
            print(f"Применение снятия: {-transaction}")
        balance += transaction
    print(f"Финальный баланс: {balance}")

apply_transactions(transactions)