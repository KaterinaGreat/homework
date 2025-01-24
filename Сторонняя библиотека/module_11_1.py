import requests
import pandas
import matplotlib
from pprint import pprint

URL = 'https://cosmetolog-kate.ru/page_kate#services'
r = requests.get(URL)
json_flag = False
if r.ok:
    try:
        r = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Содержимое ответа не в формате json.', 'От источника был получен следующий ответ:',
              r, sep='\n')
    else:
        json_flag = True
pprint(r.headers['Услуги'])


