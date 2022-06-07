import requests
import json

my_res_dead = requests.get('https://www.breakingbadapi.com/api/death')
data_dead = json.loads(my_res_dead.text)

my_res_episode = requests.get('https://breakingbadapi.com/api/episodes')
data_episode = json.loads(my_res_episode.text)

id_dead = max(data_dead, key=lambda item: item['number_of_deaths'])

result = list(filter(lambda x: x["season"] == str(id_dead["season"]) and
                     x["episode"] == str(id_dead["episode"]), data_episode))

result_all = {'ID эпизода': result[0]['episode_id'],
              'Номер сезона': id_dead["season"],
              'Номер эпизода': id_dead["episode"],
              'Общее кол-во смертей': id_dead["number_of_deaths"],
              'Список погибших': id_dead["death"]}

for key, val in result_all.items():
    print(f'{key}: {val}')

with open('file_episode.json', 'w', encoding='utf-8') as file:
    json.dump(result_all, file, ensure_ascii=False, indent=4)
