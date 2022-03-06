from telebot import TeleBot
import functions_violet_lesson

token = '5147962010:AAG2o8SPsYHwv4sJqhND0GRUZmFkX9cONUA'

bot = TeleBot(token, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def command_start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f'Привет, {first_name}')
    insert_city_name(message)

def insert_city_name(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Введите название города: ')
    bot.register_next_step_handler(msg, reply_to_user)

def reply_to_user(message):
    chat_id = message.chat.id
    user_text = message.text

    if user_text.lower() in ['stop', '/stop']:
        bot.send_message(chat_id, 'Бот остановлен. Для запуска нажмите /start')
        return

    message_to_user = functions_violet_lesson.get_weather_by_city_name(user_text)
    msg = bot.reply_to(message, message_to_user)
    # insert_city_name(message)
    bot.register_next_step_handler(msg, reply_to_user)


print('Бот работает...')
bot.polling()