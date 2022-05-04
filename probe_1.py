# 1. Создать класс TrafficLight (светофор).
# Определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        if color.lower() in ['красный', 'жёлтый', 'зелёный']:
            self.__color = color.title()
            print(True)
        else:
            raise ValueError('Недопустимое значение цвета')

    def running(self):
        print(self.__color)
        for _ in range(10):
            if self.__color == 'Красный':
                sleep(7)
                self.__color = 'Жёлтый'
                print(self.__color)
            elif self.__color == 'Жёлтый':
                sleep(2)
                self.__color = 'Зелёный'
                print(self.__color)
            elif self.__color == 'Зелёный':
                sleep(5)
                self.__color = 'Красный'
                print(self.__color)


traffic_light = TrafficLight('красный')
traffic_light.running()

