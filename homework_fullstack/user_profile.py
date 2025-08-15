user_name = input("Введите ваше имя:")

profession = input("Введие вашу профессию:")

tool = input("Введите ваш любимый инструмент для тестирования:")
if not tool:
	print("Инструмент не указан. Попробуйте снова!")
else:
	print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")

print("\n--- Резюме ---")
print(f"Имя: {user_name}")
print(f"Профессия: {profession}")
print(f"Ващ любиый инструмент в QA: {tool} .")
