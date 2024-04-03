import json
import telebot,requests
from config import keys
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(coin_1:str,coin_2:str,quantity:float):

        if coin_1 == coin_2:
            raise ConvertionException(f'Невозможно использовать одинаковые валюты "{coin_1}"')

        try:
            quote_coin_1 = keys[coin_1]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{coin_1}"')

        try:
            base_coin_2 = keys[coin_2]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{coin_2}"')

        try:
            quantity = float(quantity)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество "{quantity}"')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={keys[coin_1]}&tsyms={keys[coin_2]}&api_key=905ae94621e975906b1e318507f0686af463877ebc2809d37c953e4a26e051e2')
        total_base = json.loads(r.content)[keys[coin_2]]
        return total_base