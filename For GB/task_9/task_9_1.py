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
        self._color = color.title()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        if color.lower() in ['красный', 'жёлтый', 'зелёный']:
            self._color = color.title()
        else:
            raise ValueError('Недопустимое значение цвета')

    def running(self):
        print(self._color)
        while True:
            if self._color == 'Красный':
                sleep(7)
                self._color = 'Жёлтый'
                print(self._color)
            elif self._color == 'Жёлтый':
                sleep(2)
                self._color = 'Зелёный'
                print(self._color)
            elif self._color == 'Зелёный':
                sleep(3)
                self._color = 'Красный'
                print(self._color)


traffic_light = TrafficLight('красный')
traffic_light.color = 'зелёный'
traffic_light.running()
