import telebot
from exch_api import ExchangeVal
from config import TOKEN, keys
from Exception_ex import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду в следующем формате: \n' \
           '<имя валюты> <в какую валюту перевести> <количество переводимой валюты \n' \
           'Например: "доллар рубль 100" \n' \
           'Чтобы увидеть список всех доступных валют введите /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n-> '.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def exchange(message: telebot.types.Message):
    req = message.text.lower().split()
    if req[0] in keys and req[1] in keys and len(req) == 3 and req[2].isdigit()\
            and req[0] != req[1]:
        bot.reply_to(message, f'Результат конвертации: '
                              f'{ExchangeVal.get_price(keys.get(req[0]), keys.get(req[1]), float(req[2]))}')
    else:
        bot.reply_to(message, 'Введены неправильные значения, попробуйте снова!')


bot.polling(none_stop=True)
