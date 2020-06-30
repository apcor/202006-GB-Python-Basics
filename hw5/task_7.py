import json


with open('task_7_file.txt', 'r', encoding='utf-8') as source_file:
    firms_data = [line.strip().split() for line in source_file]

# print out a column of profit statements
pos_profits = []
for el in firms_data:
    el[2] = int(el[2]) - int(el[3])
    print(f'Прибыль фирмы {el[1]} {el[0]} равна {el[2]}')
    if el[2] >= 0:
        pos_profits.append(el[2])

# print out average profits
av_profits = sum(pos_profits) / len(pos_profits)
print(f'\nСредняя прибыль безубыточных фирм равна {av_profits:.2f}')

# create a list with two dicts inside
res_list = [{el[0]: el[2] for el in firms_data}, {'average_profit': av_profits}]

# create and open a new json file and write the list
with open('task_7_file.json', 'w', encoding='utf-8') as end_file:
    json.dump(res_list, end_file)

