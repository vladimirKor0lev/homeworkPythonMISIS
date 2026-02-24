limit = int(input("До какого числа мы считаем?"))
sum_of_num = limit * (limit+1)/2
if sum_of_num == int(sum_of_num):
    sum_of_num = int(sum_of_num)
print(f"Сумма положительных чисел от 1 до {limit} равна {sum_of_num}")