# Интернет-магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите программу, запрашивающую у пользователя количество тех и других покупок, после чего выведите на экран общий вес посылки.
mass_of_souvenir = 75
mass_of_useless = 112
souvenir_amount, useless_amount = [
    int(i)
    for i in input("Введите количество сувениров и безделушек\n").split()
    ]
revenue = souvenir_amount * mass_of_souvenir + useless_amount * mass_of_useless
print(f"{revenue} grams")