# Задача 2. Сортировка
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке:
# его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их.
# Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name, surname, age, salary):
        self._name = name
        self._surname = surname
        self._age = age
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self._age = age
        else:
            print('Некорректный возраст')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print('Некорректное значение зарплаты')


tom = Person(name='Tom', surname='White', age=25, salary=2000)
mike = Person(name='Mike', surname='Black', age=23, salary=2500)
kate = Person(name='Kate', surname='Sun', age=22, salary=1700)

list_person = [tom, mike, kate]

sort_list = sorted(list_person, key=lambda elem: elem.salary)

for element in sort_list:
    print(element.name)
