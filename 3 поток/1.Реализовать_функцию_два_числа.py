# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dva(*args):
    try:
        arg1 = int(input("Введите делитель: "))
        arg2 = int(input("Введите делитель: "))
        res = arg1 / arg2
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Значение не может быть равно нулю")
print(f'Результат: {dva()}')