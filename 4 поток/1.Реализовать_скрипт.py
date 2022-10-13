# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


if len(argv) > 1:
    script, time, rate,prize = argv
    time = int(time)
    rate = int(rate)
    prize = int(prize)
    print((time * rate) + prize)
else:
    time = int(input("Выработка в часах: "))
    rate = int(input("Ставка в час: "))
    prize = int(input("Премия: "))
    print((time * rate) + prize)
