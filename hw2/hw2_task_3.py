'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.'''

user_num = int(input('Введите номер месяца: '))

seasons_list = [[12, 1, 2, 'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]
seasons_dict = {
    (12, 1, 2): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень',
}

for el in seasons_list:
    if user_num in el:
        print(el[3])

for el in seasons_dict.keys():
    if user_num in el:
        print(seasons_dict[el])

