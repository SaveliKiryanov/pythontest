n = int(input("Введите число: "))

print("Числа:", *range(1, n + 1))

total = sum(range(1, n + 1))
print("Сумма чисел:", total)
