name = input("Введите ваше имя: ")
profession = input("Введите вашу профессию: ")

years_in_qa = input("Сколько лет вы работаете в QA? ")

answer = input("Что такое переменная? ")

keywords = ["значение", "хранит", "данные", "памяти", "объект"]

if any(word.lower() in answer.lower() for word in keywords):
    print(f"\nОтлично, {name}! Похоже, вы понимаете, что такое переменная.")
else:
    print(f"\n{name}, переменная — это по сути именованная область памяти для хранения данных.")

print("\n--- Резюме ---")
print(f"Имя: {name}")
print(f"Профессия: {profession}")
print(f"Опыт в QA: {years_in_qa} лет")