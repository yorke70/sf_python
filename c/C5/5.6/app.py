import telebot
from exch_api import convert

TOKEN = '5483108626:AAEbqQ0AQJYVFmDTQUecnIXID9wgDp5t8V0'
keys = {
    "рубль" : "RUB",
    "доллар" : "USD",
    "евро" : "EUR",
    "фунт" : "GBP",
    "Йена" : "JPY",
    "юань" : "CNY"
}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду в следующем формате: \n' \
           '<имя валюты> <в какую валюту перевести> <количество переводимой валюты \n' \
           'Например: "доллар рубль 100" \n' \
           'Чтобы увидеть всех достпных валют введите /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n-> '.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def exchange(message: telebot.types.Message):
    zapros = message.text.lower().split()
    if zapros[0] in keys and zapros[1] in keys and zapros[2].isdigit():
        bot.reply_to(message, f'Результат конвертации: '
                              f'{convert(keys.get(zapros[0]), keys.get(zapros[1]), float(zapros[2]))}')
    else:
        bot.reply_to(message, 'Введены неправильные значения, попробуйте снова!')

bot.polling(none_stop=True)
