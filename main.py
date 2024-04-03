import json
import telebot,requests
from config import keys,TOKEN
from extensions import ConvertionException,CryptoConverter


bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help'])
def start_message(message:telebot.types.Message):
    bot.send_message(message.chat.id,'Здравствуйте! Для получения \n'
                                          'информации об использованиие\n'
                                          'бота введите /start или /help\n'
                                          'Просмотреть список всех валют /values\n')

@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text='Доступные валюты:'
    for i,key in enumerate(keys):
        text+=f'\n {i+1}.{key}'
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert(message:telebot.types.Message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise ConvertionException(f'Количество параметров должно равняться 3!')
        coin_1,coin_2,quantity=values
        total_base=CryptoConverter.get_price(coin_1,coin_2,quantity)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')

    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду:\n{e}')
    else:
        text=f'Цена {quantity} {coin_1} в {coin_2} = {float(total_base)*float(quantity)} '
        bot.reply_to(message,text)


bot.polling(none_stop=True)

