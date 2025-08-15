days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
test_cases = []

for day in days:
	while True:
		try:
			count = int(input(f"Введите количество тест-кейсов за {day}:"))
			if count < 0:
				print("Количество не может быть отрицательным. Попробуйте снова.")
				continue
			test_cases.append(count)
			break
		except ValueError:
			print("Пожалуйста, введите целое число")

total_test = sum(test_cases)
average_test = total_test/len(test_cases)

print("\n--- Результаты ---")
print(f"Общее количество тестов за неделю: {total_test}")
print(f"Среднее количество тестов в день: {average_test}")

if average_test > 10:
	print("Отличная работа!")
else:
	print("Попробуйте улучшить результат")