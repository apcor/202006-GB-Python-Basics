'''Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''


with open('task_1_file.txt', 'w', encoding = 'utf-8') as my_file:
    while True:
        user_str = input('Введите строку: ')
        my_file.writelines(f'{user_str} \n')
        if user_str == '':
            break

