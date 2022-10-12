# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element_count = int(input("Введите количество элементов списка: "))
_list = []
i = 0
element = 0

while i < element_count:
    _list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(_list)/2)):
    _list[element], _list[element + 1] = _list [element + 1], _list[element]
    element += 2
    
print(_list)