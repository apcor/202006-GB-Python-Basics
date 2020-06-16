# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input('Enter a positive integer: '))
dummy_var = user_num
max_digit = dummy_var % 10
while dummy_var > 0:
    if dummy_var % 10 >= max_digit:
        max_digit = dummy_var % 10
        if max_digit == 9:
            break
    dummy_var = dummy_var // 10
print(f'The maximum digit in {user_num} is {max_digit}')



