def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Треугольник равносторонний."
        elif a == b or a == c or b == c:
            return "Треугольник равнобедренный."
        else:
            return "Треугольник разносторонний."
    else:
        return "Треугольник с такими сторонами не существует."
a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))

print("Результат:", check_triangle(a, b, c))
