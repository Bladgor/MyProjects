# Задача 3. Во все тяжкие
# Что нужно сделать
# Фанаты сериала Breaking Bad («Во все тяжкие») написали собственный API по вселенной своего любимого сериала.
# Ссылка на документацию: Document At ion.
#
# Внимательно изучите документацию этого API и напишите программу,
# которая выводит на экран (а также в JSON-файл) информацию о том, в каком эпизоде произошло больше всего смертей.
# Информация хранится в виде словаря, который содержит:
#
# ID эпизода.
# Номер сезона.
# Номер эпизода.
# Общее количество смертей.
# Список погибших.
#
# Что оценивается
# Результат вычислений корректен.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'

my_req = requests.get(url)
data = json.loads(my_req.text)

# episodes_url = data["episodes"]
# episodes_req = requests.get(episodes_url)
# episodes = json.loads(episodes_req.text)

with open('breaking.json', 'w') as file:
    json.dump(data, file, indent=4)


