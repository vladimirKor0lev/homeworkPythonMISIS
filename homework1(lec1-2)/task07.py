#Дано двузначное и трехзначное число.
#Для каждого выведите на экран сумму и произведение цифр.
import math
def digit_sum(number: int):
    digit_list = list(map(int, str(number)))
    return sum(digit_list)
def digit_prod(number: int):
    digit_list = list(map(int, str(number)))
    return math.prod(digit_list)
number1, number2 = map(int, input("Введите два числа через пробел: \n").split())
output_str = """
Результат
# Первое число
Сумма цифр первого числа равна {sum1}
Произведение цифр первого числа равна {prod1}
# Второе число
Сумма цифр второго числа равна {sum2}
Произведение цифр второго числа равна {prod2}
"""
print(output_str.format(sum1 = digit_sum(number1), sum2 = digit_sum(number2), prod1 =digit_prod(number1), prod2 = digit_prod(number2)))
