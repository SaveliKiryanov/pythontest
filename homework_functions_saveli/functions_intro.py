def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum(a, b):
    return a + b
name = input("Введите ваше имя: ")
greet_user(name)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = calculate_sum(a, b)
print(f"Сумма чисел: {result}")