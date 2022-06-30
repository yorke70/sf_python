import requests
import json
from Exception_ex import *


API_KEY = 'e3c5769799976f403f760cf2b0edf760'
BASE = 'https://currate.ru/api/?get=rates&pairs='


class ExchangeVal:
    @staticmethod
    def get_price(base, quote, amount):
        r = requests.get(BASE + base + quote + '&key=' + API_KEY).content
        r = json.loads(r)
        cur = 0

        # try:
        #     amount.isdigit()
        # except ValueError:
        #     raise APIException("Указано неверное количество для обмена")

        if str(r.get('status')) == '200':
            cur = float(r['data'][str(base + quote)])
            exch = round(cur * float(amount), 2)
            print(f'Запрос валютной пары {base + quote}. Результат обмена {exch}')
            return exch
        else:
            print('Ошибка ввода, нужно попробовать другую валютную пару')
            return None


if __name__ == '__main__':
    ExchangeVal.get_price('USD', 'CNY', '100')
    ExchangeVal.get_price('USD', 'CNY', '1d')
