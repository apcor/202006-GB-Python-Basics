'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка,
определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
'''


from itertools import count, cycle

start_int = 8
end_int = 25

for el in count(start_int):
    if el > end_int:
        break
    else:
        print(el, end=' ')
print()

counter = 0
for el in cycle(['a', 'b', 'c', 'd', 'e', 'f']):
    if counter > end_int:
        break
    else:
        print(el, end='_')
        counter += 1
