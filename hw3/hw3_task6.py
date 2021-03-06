'''Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из
латинских букв в нижнем регистре.
Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(text):
    return text.capitalize()


user_word = input('Введите слово в нижнем регистре: ')
print(int_func(user_word))

user_str = list(map(int_func, input('Введите строку из слов в нижнем регистре через пробел: ').split()))
print(*user_str)
