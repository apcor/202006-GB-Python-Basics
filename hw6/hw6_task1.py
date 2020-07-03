'''Создать класс TrafficLight (светофор) и
определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и
вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
'''


import time


class TrafficLight:

    def __init__(self):
        self.__color = None
        self.pattern = ['red', 'yellow', 'green']
        self.running()

    def set_color(self, color, period):
        self.__color = color
        print(f'Traffic light is: {color}')
        time.sleep(period)

    def running(self):
        try:
            if self.pattern == ['red', 'yellow', 'green']:
                self.set_color(self.pattern[0], 7)
                self.set_color(self.pattern[1], 2)
                self.set_color(self.pattern[2], 5)
            else:
                raise Exception('Wrong color order')
        except Exception as e:
            exit(e)


a = TrafficLight()
