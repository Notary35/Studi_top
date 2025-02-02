import telebot

# Вставьте сюда ваш токен от @BotFather
TOKEN = "8122692273:AAH-TLwdFymR78NXkL-GqlbcZT8m4wIC7MU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Ваш chat_id: {chat_id}")
    print(f"Chat ID пользователя: {chat_id}")

print("Бот запущен! Отправьте команду /start")
bot.polling()
