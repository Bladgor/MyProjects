import requests
import json
from pprint import pprint

# url = "https://hotels4.p.rapidapi.com/properties/list"
#
# querystring = {"destinationId": "549499", "pageNumber": "2", "pageSize": "25", "checkIn": "2022-12-14",
#                "checkOut": "2022-12-16", "adults1": "1", "sortOrder": "PRICE", "locale": "ru_RU", "currency": "RUB"}
#
# headers = {
#     "X-RapidAPI-Key": "9adf9fc99fmsh6713e606247ad93p17623ejsn60318b0a84af",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.encoding)
# data = json.loads(response.text)
#
# with open('hotel.json', 'w') as f:
#     json.dump(data, f, indent=4)

with open('hotel.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    print(data['data']['body']['searchResults']['results'][0]['ratePlan']['price']['exactCurrent'])

list_price = []
hotels_dict = dict()
data_price = data['data']['body']['searchResults']['results']

for elem in data_price:
    list_price.append(elem['ratePlan']['price']['exactCurrent'])

print(list_price)
print(len(list_price))

# TODO сделать словарь вместо list_price
