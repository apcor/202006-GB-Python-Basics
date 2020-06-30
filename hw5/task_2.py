# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2_file.txt', 'r', encoding='utf-8') as my_file:
    qty_lines = 0
    for idx, line in enumerate(my_file, 1):
        print(f'В строке №{idx}  -  {len(line.split())} слов.')
    print(f'Количество строк в файле {my_file.name} - {idx}.')

