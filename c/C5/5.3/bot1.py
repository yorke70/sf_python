import telebot


bot = telebot.TeleBot('5368648356:AAEt7oV6a-R4HdtB9YwDWzWTKY-J5-lLhzE')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
