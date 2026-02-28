# Дано уравнение ax + b = 0 и отрезок [m;n].
# Ответьте на вопрос, попадает ли решение уравнения в указанный отрезок.
a, b, m, n = map(float, input("Введите a b m n: ").split())
left = min(m, n)
right = max(m, n)

if a == 0:
    if b == 0:
        print("Бесконечно много решений")
    else:
        print("Решений нет")
else:
    x = -b / a

    if left <= x <= right:
        print("Решение попадает в отрезок")
    else:
        print("Решение НЕ попадает в отрезок")
