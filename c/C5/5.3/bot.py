import telebot

TOKEN = "5368648356:AAEt7oV6a-R4HdtB9YwDWzWTKY-J5-lLhzE"

bot = telebot.TeleBot('5368648356:AAEt7oV6a-R4HdtB9YwDWzWTKY-J5-lLhzE')

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass


# Обрабатывается все документы и аудиозаписи


# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass
#

@bot.message_handler(commands=['start', 'help'])
def handle_reply_username(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.username}')
    print("Введена команда /start или /help")


@bot.message_handler(content_types=['photo', ])
def handle_reply_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')
    print("Бот получил фото")


bot.polling(none_stop=True)
