# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.


user_inp = int(input('Введите число: '))
# simplifying   digit_sum = user_inp + 10 * user_inp + user_inp + 100 * user_inp + 10 * user_inp + user_inp
digit_sum = 123 * user_inp
print(digit_sum)


