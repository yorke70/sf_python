import requests
import json


API_KEY = 'e3c5769799976f403f760cf2b0edf760'
BASE = 'https://currate.ru/api/?get=rates&pairs='


def convert(val1, val2, num=1):
    r = requests.get(BASE+val1+val2+'&key='+API_KEY).content
    r = json.loads(r)
    cur = float(r['data'][str(val1+val2)])
    exchange = cur * num
    print(f'Запрос валютной пары {val1+val2}. Результат обмена {exchange}')
    return exchange

if __name__ == '__main__':
    convert('USD', 'CNY', 100)
