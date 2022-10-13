# 5. Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {list}")
digit = int(input("Для выхода, вызывайте 911: "))
while digit != 911:
    for el in range(len(list)):
        if list[el] == digit:
            list.insert(el + 1, digit)
            break
        elif list[0] < digit:
            list.insert(0, digit)
        elif list[-1] > digit:
            list.append(digit)
        elif list[el] > digit and list[el + 1] < digit:
            list.insert(el + 1, digit)
    print(f"Текущий список - {list}")
    digit = int(input("Для выхода, вызывайте 911: "))