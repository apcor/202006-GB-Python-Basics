with open('task_4_file.txt', 'r', encoding='utf-8') as source_file:
    source_data = source_file.read().splitlines()

ref_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять',
    }

new_data = []
for eng_num in ref_dict.keys():
    for n in source_data:
        if eng_num in n:
            new_data.append(n.replace(eng_num, ref_dict[eng_num]))


with open('task_4_file_new.txt', 'w', encoding='utf-8') as end_file:
    for el in new_data:
        end_file.writelines(f'{el}\n')

