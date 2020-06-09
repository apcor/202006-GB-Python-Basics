# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные,
# выведите на экран.

my_num = 5
my_float = 0.66

print(f'My number is {my_num}, my float is {my_float}')

user_str = input('Please enter a string: ')
user_float = float(input('Please enter a decimal number: '))
print('You entered a string %s and a decimal number %f' % (user_str, user_float))

user_bool = bool(int(input('Enter 0 or 1: ')))
print('You entered {}'.format(user_bool))



