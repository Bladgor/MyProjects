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
