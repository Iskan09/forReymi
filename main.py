import telebot
from telebot import types

bot = telebot.TeleBot('8141145179:AAFiOeLTE2hWPsdfRFN9WBaNA5_PxvaCoN0')
user=5983


@bot.message_handler(commands=['start'])
def main(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('Пепперони',callback_data='peperoni')
    btn2=types.InlineKeyboardButton('Маргарита',callback_data='margarita')
    btn3=types.InlineKeyboardButton('Четыре сыра',callback_data='four_cheeses')
    btn4=types.InlineKeyboardButton('Сырный цыпленок',callback_data='chicken_cheese')
    markup.row(btn1, btn2, btn3, btn4)
    file = open('./pizza.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id,'Здравствуйте,выберетете пожалуйста пиццу которую вы хотите заказать', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'peperoni':
        bot.send_message(call.message.chat.id, '🍕Вы выбрали Пепперони!')
    elif call.data == 'margarita':
        bot.send_message(call.message.chat.id, '🍕Вы выбрали Маргариту!')
    elif call.data == 'four_cheeses':
        bot.send_message(call.message.chat.id, '🍕Вы выбрали Четыре сыра!')
    elif call.data == 'chicken_cheese':
        bot.send_message(call.message.chat.id, '🍕Вы выбрали Сырный цыпленок!')


bot.polling(none_stop=True, interval=0)
