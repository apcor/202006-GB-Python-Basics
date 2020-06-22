''' Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление. Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
'''

def my_div(num1, num2):
    try:
        print(f'{num1} divided by {num2} equals {num1 / num2}')
    except ZeroDivisionError:
        print('Division by 0 not allowed')


user_num1 = int(input('Enter number 1: '))
user_num2 = int(input('Enter number 2: '))

my_div(user_num1, user_num2)
