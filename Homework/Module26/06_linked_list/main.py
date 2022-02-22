# ## Задача 6. Односвязный список
# Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать Односвязный список.
#
# Связный список — это структура данных, которая состоит из элементов, зовущихся узлами.
# В узлах хранятся данные, а между собой узлы соединены связями.
# Связь – это ссылка на следующий или предыдущий элемент списка.
#
# ![task_06_pic](linkedlist.png)
#
# В односвязном списке связь - это ссылка только на следующий элемент.
# То есть в нём можно передвигаться только в сторону конца списка.
# Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.
#
# Реализуйте такую структуру данных без использования стандартных структур Питона
# (list, dict, tuple и прочие) и дополнительных модулей.
#
# Для структуры реализуйте следующие методы:
# - append - добавление элемента в конец списка
# - get - получение элемента по индексу
# - remove - удаление элемента по индексу
#
# Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла
#
# #### Пример основной программы:
# ````python
# my_list = LinkedList()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)
# ````
#
# #### Результат:
# ````
# Текущий список: [10 20 30]
# Получение третьего элемента: 30
# Удаление второго элемента.
# Новый список: [10 30]
# ````
# TODO Моя беда с аннотациями продолжается. Прошу советов по исполнению.

from typing import Optional, Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.index = -1

    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(value)

    def get(self, search_index: int) -> Optional[Any]:
        last = self.head
        data_index = 0
        while search_index != data_index:
            if last.next is None and search_index != data_index:
                return None
            data_index += 1
            last = last.next
        return last.data

    def remove(self, remove_index: int) -> None:
        prev = self.head
        current = self.head
        data_index = 0
        while remove_index != data_index:
            if current.next is None and remove_index != data_index:
                print('Такого индекса нет')
                return
            data_index += 1
            prev = current
            current = current.next
        prev.next = current.next

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self) -> Optional[Any]:
        self.index += 1
        if self.get(self.index) is not None:
            return self.get(self.index)
        else:
            raise StopIteration

    def __str__(self) -> str:
        if self.head is None:
            return '[]'
        text = '['
        last = self.head
        while last.next:
            if text.endswith('['):
                text += f'{last.data}'
            else:
                text += f' {last.data}'
            last = last.next
        text += f' {last.data}]'
        return text


my_list = LinkedList()
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append('abc')

print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
my_list.remove(5)
