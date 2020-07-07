'''Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''


class Cell:

    def __init__(self, unit_num):
        try:
            if unit_num > 0:
                self.unit_num = unit_num
            else:
                raise Exception('Отрицательное кол-во ячеек!')
        except Exception as e:
            print(e)

    def __str__(self):
        return f'Клетка  [{"*" * self.unit_num}]'

    def __add__(self, other):
        sum_units = self.unit_num + other.unit_num
        return Cell(sum_units)

    def __sub__(self, other):
        try:
            dif_units = self.unit_num - other.unit_num
            return Cell(dif_units)
        except Exception as e:
            print('Нельзя вычесть клетки!', e)

    def __mul__(self, other):
        mul_units = self.unit_num * other.unit_num
        return Cell(mul_units)

    def __truediv__(self, other):
        div_units = self.unit_num // other.unit_num
        return Cell(div_units)

    def make_order(self, row_units):
        print(f'[', end='')
        for idx in range(self.unit_num // row_units):
            print(f'{"*" * row_units}')
        print(f'{"*" * (self.unit_num % row_units)}]')


if __name__ == '__main__':
    cell_1 = Cell(27)
    cell_1.make_order(11)
    cell_2 = Cell(5)
    print(cell_2 - cell_2)
