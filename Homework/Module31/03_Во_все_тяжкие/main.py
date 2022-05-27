# Задача 3. Во все тяжкие
# Что нужно сделать
# Фанаты сериала Breaking Bad («Во все тяжкие») написали собственный API по вселенной своего любимого сериала.
# Ссылка на документацию: Document At ion.
#
# Внимательно изучите документацию этого API и напишите программу,
# которая выводит на экран (а также в JSON-файл) информацию о том, в каком эпизоде произошло больше всего смертей.
# Информация хранится в виде словаря, который содержит:
#
# 1. ID эпизода.
# 2. Номер сезона.
# 3. Номер эпизода.
# 4. Общее количество смертей.
# 5. Список погибших.
#
# Что оценивается
# Результат вычислений корректен.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import requests
import json

if __name__ == '__main__':
    episodes_url = 'https://www.breakingbadapi.com/api/episodes'
    episodes_req = requests.get(episodes_url)
    episodes = json.loads(episodes_req.text)

    death_url = 'https://www.breakingbadapi.com/api/death'
    death_req = requests.get(death_url)
    death = json.loads(death_req.text)

    max_death = max(death, key=lambda x: x["number_of_deaths"])

    episode_max_death = dict()
    for elem in episodes:
        if elem['season'] == str(max_death['season']) and elem['episode'] == str(max_death['episode']):
            episode_max_death['episode_id'] = elem['episode_id']
            break

    episode_max_death['season'], episode_max_death['episode'], episode_max_death['number_of_deaths'] = \
        max_death['season'], max_death['episode'], max_death['number_of_deaths']
    episode_max_death['death'] = max_death['death']

    with open('episode_max_death.json', 'w') as file:
        json.dump(episode_max_death, file, indent=4)
