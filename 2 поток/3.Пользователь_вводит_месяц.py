# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

_list = ['Зима', 'Весна', 'Лето', 'Осень']
_dict = {12 : 'Декабрь', 1 : 'Январь', 2 : 'Февраль', 
        3 : 'Март', 4 : 'Апрель', 5 : 'Май', 
        6 : 'Июнь', 7 : 'Июль', 8 : 'Август', 
        9 : 'Сентябрь', 10 : 'Октябрь', 11 : 'Ноябрь'}
month = int(input("Введите месяц по номеру: "))
if month == 12:           
    print(_list[0])
    print(_dict.get(12)) 
elif month == 1:          
    print(_list[0])
    print(_dict.get(1))  
elif month == 2:
    print(_list[0])
    print(_dict.get(2)) 
elif month == 3:
    print(_list[1])
    print(_dict.get(3))  
elif month == 4:
    print(_list[1])
    print(_dict.get(4))  
elif month == 5:
    print(_list[1])
    print(_dict.get(5))  
elif month == 6:
    print(_list[2])
    print(_dict.get(6))  
elif month == 7:
    print(_list[2])
    print(_dict.get(7))  
elif month == 8:
    print(_list[2])
    print(_dict.get(8))  
elif month == 9:
    print(_list[3])
    print(_dict.get(9)) 
elif month == 10:
    print(_list[3])
    print(_dict.get(10)) 
elif month == 11:
    print(_list[3])
    print(_dict.get(11)) 
else:
    print("Такого месяца не существует")