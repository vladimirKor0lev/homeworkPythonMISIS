#Представьте, что вы пишете программное обеспечение для автоматической кассы в магазине самообслуживания. Одной из функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными.
#Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. После этого она должна рассчитать и вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть задействовано минимально возможное количест­во монет. Допустим, у нас есть в распоряжении монеты достоинством в 1, 5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.

change_to_give =float(input("Введите сумму сдачи, разделяйте через точку:"))
change_to_give = int(change_to_give*100)
toonies = 0
loonies = 0
quarters = 0
tens = 0
fives = 0
ones = 0
rest_of_change_to_give = change_to_give
if rest_of_change_to_give >= 200:
    toonies = rest_of_change_to_give//200
    rest_of_change_to_give = rest_of_change_to_give - 200*toonies
if rest_of_change_to_give >= 100:
    loonies = rest_of_change_to_give//100
    rest_of_change_to_give = rest_of_change_to_give - 100*loonies
if rest_of_change_to_give >= 25:
    quarters = rest_of_change_to_give//25
    rest_of_change_to_give = rest_of_change_to_give - 25*quarters
if rest_of_change_to_give >= 5:
    fives = rest_of_change_to_give//5
    rest_of_change_to_give = rest_of_change_to_give - 5*fives
if rest_of_change_to_give != 0:
    ones = rest_of_change_to_give
print (f"You need to give {toonies} toonies, {loonies} loonies, {quarters} quarters, {fives} fives,{ones} single cent coins")


