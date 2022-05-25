# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API, посвящённый вселенной Star Wars.
# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).
# Затем напишите программу, которая парсит данные об этом человеке,
# изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла.
#
# Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
# В том же коде спарсите эту ссылку и посмотрите, что там.
#
# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать,
# поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.

import requests
import json
from pprint import pprint

url = 'https://swapi.dev/api/people/3/'

my_req = requests.get(url)

data = json.loads(my_req.text)
data['name'] = 'Vitaly'

with open('my_first_json.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('my_first_json.json') as file:
    data = json.load(file)
    pprint(data)
    print('=' * 60)
    url = data['homeworld']
    my_req = requests.get(url)
    homeworld = json.loads(my_req.text)
    pprint(homeworld)
