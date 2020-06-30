import random

with open('task_5_file.txt', 'w', encoding='utf-8') as write_file:
    for _ in range(random.randint(5, 15)):
        write_file.write(f'{random.randint(1, 1000)} ')

with open('task_5_file.txt', 'r', encoding='utf-8') as read_file:
    print(f'Сумма чисел в файле {read_file.name} равна '
          f'{sum(list(map(int, read_file.read().split())))}')


