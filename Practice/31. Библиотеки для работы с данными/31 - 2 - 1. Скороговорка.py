# Задача 1. Скороговорка
# Дан текст вот такой английской скороговорки:
# How much wood would a woodchuck chuck if a woodchuck could chuck wood?
#
# С помощью модуля re реализуйте программу, которая выполняет следующие действия по порядку:
#
# Определить, начинается ли текст с шаблона wo.
# Найти первое упоминание шаблона wo в тексте.
# Определить содержимое найденной по шаблону подстроки из пункта 2.
# Найти позицию, с которого начинается первое упоминание шаблона wo.
# Найти позицию, на которой заканчивается первое упоминание шаблона wo.
# Получить список из каждого упоминания шаблона wo в тексте.
# Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».
# По каждому действию вывести соответствующий результат.
# Не используйте методы строк.
# Не забывайте использовать приписку r в шаблонах.
#
# Ожидаемый результат работы программы:
#
# Поиск шаблона в начале строки: None
# Поиск первого найденного совпадения по шаблону: <re.Match object; span=(9, 11), match='wo'>
# Содержимое найденной подстроки: wo
# Начальная позиция: 9
# Конечная позиция: 11
# Список всех упоминаний шаблона: ['wo', 'wo', 'wo', 'wo', 'wo']
# Текст после замены: How much ЗАМЕНАod ЗАМЕНАuld a ЗАМЕНАodchuck chuck if a ЗАМЕНАodchuck could chuck ЗАМЕНАod?

import re
text = r'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
result = re.match(r'wo', text)
print('Поиск шаблона в начале строки:', result)  # 1
result = re.search(r'wo', text)
print('Поиск первого найденного совпадения по шаблону:', result)  # 2
print('Содержимое найденной подстроки:', result.group())  # 3
print('Начальная позиция:', result.start())  # 4
print('Конечная позиция:', result.end())  # 5
result = re.findall(r'wo', text)
print('Список всех упоминаний шаблона:', result)  # 6
result = re.sub(r'wo', 'ЗАМЕНА', text)
print('Текст после замены:', result)
