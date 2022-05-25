# Задача 2. Документация API
# Обычно к открытым API прилагается подробная документация,
# где описывается логика формирования ссылок и какие данные по ним можно получать (или отправлять!).
#
# Изучите документацию того же сайта по «Звёздным войнам».
#
# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.
# А ещё попробуйте библиотеку swapi (о ней также в документации)
# и с её помощью выведите начало сюжета из фильма «Новая надежда» (A New Hope).

import requests
import json
from pprint import pprint

url = 'https://swapi.dev/api/'

my_req = requests.get(url)
data = json.loads(my_req.text)
films_url = data['films']
films_req = requests.get(films_url)
films = json.loads(films_req.text)
with open('films.json', 'w') as file:
    json.dump(films, file, indent=4)

with open('films.json') as file:
    data = json.load(file)
    for elem in data["results"]:
        if elem["title"] == "A New Hope":
            pprint(elem)
