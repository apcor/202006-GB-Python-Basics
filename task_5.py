# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью,
# вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Enter the revenue: '))
expenses = int(input('Enter the expenses: '))

profit = revenue - expenses

if profit > 0:
    print('The firm has a profit!')
    print(f'The profit margin is {profit / revenue:.2f} ')
    empl_number = int(input('Enter the number of employees: '))
    print(f'Profit per employee is {profit / empl_number:.3f}')
elif profit < 0:
    print('The firm has a loss!')
else:
    print('The firm breaks even')

