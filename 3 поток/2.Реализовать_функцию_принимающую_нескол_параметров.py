# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name1 = input('Введите имя: ')
surname1 = input('Введите фамилия: ')
data1 = input('Введите год рождения: ')
city1 = input('Введите город: ')
email1 = input('Введите Email: ')
phone1 = input('Введите телефон: ')

def info(name, surname,data, city,email,phone):
    return ' '.join([name, surname, data, city, email, phone])
print(info(surname=surname1, name=name1, data=data1, city=city1, email=email1, phone=phone1))