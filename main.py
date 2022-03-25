import telebot
import random
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5284333469:AAFfkpkMTum-Lj3uRgF2_zbH9s-BdDLrC70')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = 'Это факт'
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
            answer = 'Это поговорка'
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

def plus(a,b):
    return a+b

# Запускаем бота
bot.polling(none_stop=True, interval=0)