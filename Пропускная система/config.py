import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к. отсутствует файл .env')
else:
    load_dotenv()

API_KEY = os.getenv('API_KEY')
terminal_name = 'terminal1'
url = f'https://pass.mosgt.ru/api/test.php?api_key={API_KEY}&terminal={terminal_name}'
# url = f'https://yandex.ru/search/?text=некоторые+строки+другим+цветом+в+таблице+pysimplegui&lr=214019'
timeout = 1000
font_size = 20
