import requests
import json
from config import keys
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
#        values = message.text.split(' ')
        if quote == base:
           raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticer = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}.')
        try:
            base_ticer = keys[base]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалос обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticer}&tsyms={base_ticer}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base