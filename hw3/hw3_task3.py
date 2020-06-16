'''Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.'''


def my_func(var1, var2, var3):
    dummy_list = [var1, var2, var3]
    return sum(sorted(dummy_list, reverse=True)[:2])


u_num1, u_num2, u_num3 = map(int, input('Enter 3 spaced numbers: ').split())
print(f'The sum of the largest two numbers is {my_func(u_num1, u_num2, u_num3)}')
