'''Реализовать скрипт, в котором должна быть
предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
'''

import sys


def income_calc(hours, wage, bonus=0):
    income = float(hours) * float(wage) + float(bonus)
    print(income)


try:
    income_calc(*sys.argv[1:])
except TypeError as e:
    print('Enter at least hours and wage as parameters, bonus is optional ', e)
