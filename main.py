import telebot
from telebot import types

from request import check_weather

bot = telebot.TeleBot('5695601211:AAGl4SQEzpiPX1L5LxCw6K18gvx7iabJudw')

CITY_LIST = ['Cherkasy', ' Chernihiv', 'Chernivtsi', 'Dnipro', 'Donetsk', 'Ivano-Frankivsk', 'Kharkiv', 'Kherson',
             'Khmelnytskyi,', 'Kropyvnytskyi', 'Kyiv', 'Luhansk', 'Lutsk', 'Lviv', 'Mykolaiv', 'Odesa', 'Poltava',
             'Rivne', 'Sumy', 'Ternopil', 'Uzhhorod', 'Vinnytsia', 'Zaporizhzhia', 'Zhytomyr']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, хочешь узнать погоду?")
        keyboard = types.InlineKeyboardMarkup()
        for i in CITY_LIST:
            key_oven = types.InlineKeyboardButton(text=i, callback_data=i)
            keyboard.add(key_oven)
        bot.send_message(message.from_user.id, text='Выбери город в меню или напиши его', reply_markup=keyboard)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        ms = check_weather(message.text)
        msg = f"Погода в {message.text} - {ms}"
        bot.send_message(message.from_user.id, msg)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    ms = check_weather(call.data)
    msg = f"Погода в {call.data} - {ms}"
    bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)


