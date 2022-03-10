# ## Задача 4. Дата
# Реализуйте класс Date, который должен уметь:
# - Проверять числа даты на корректность
# - Конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года
#
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
# При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации,
# например:
# ````python
# date = Date.from_string('10-12-2077')
# ````
# Неверный вариант:
# ````python
# date = Date(10, 12, 2077)
# ````
#
# #### Пример основного кода:
# ````python
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# ````
#
# #### Результат:
# ````
# День: 10	Месяц: 12	Год: 2077
# True
# False
# ````

from typing import Any


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def from_string(cls, date: str) -> Any:
        if cls.is_date_valid(date):
            day, month, year = map(int, date.split('-'))
            date_object = cls(day, month, year)
            return date_object
        else:
            raise ValueError('Недопустимое значение')

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        date = date.split('-')
        if len(date) != 3:
            return False
        else:
            day, month, year = map(int, date)
            year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                year_dict[2] = 29
            return month in year_dict and 0 < day <= year_dict[month] and 0 < year <= 9999


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('29-02-2020'))
print(Date.is_date_valid('29-02-2021'))
my_date = Date.from_string('10-122077')

# зачет!
