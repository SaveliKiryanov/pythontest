def calculator():
    # Ввод чисел
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Ошибка: деление на ноль!"
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Ошибка: неизвестная операция!"

    return result
print("Результат:", calculator())
