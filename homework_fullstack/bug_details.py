bug_report = {
    "ID": 101,
    "Название": "Ошибка входа в систему",
    "Статус": "Открыт"
}

print("Исходный баг-репорт:")
print(bug_report)

bug_report["Статус"] = "Закрыт"

print("\nОбновленный баг-репорт:")
print(bug_report)

explanation = """Неизменяемые типы данных — это такие типы, значение которых нельзя изменить после создания.
Примеры:
- int (целые числа)
- float (числа с плавающей точкой)
- str (строки)
- tuple (кортежи)
- frozenset (неизменяемые множества)"""

with open("data_types.txt", "w", encoding="utf-8") as file:
    file.write(explanation)

print("\nФайл 'data_types.txt' был создан с объяснением неизменяемых типов данных.")
