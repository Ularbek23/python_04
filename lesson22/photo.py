import telebot

TOKEN = "6935378517:AAF3ay_KYtIWKVvrBRpW1EthWNz5bWp2xJo"
chat_id = 1020812876
tg = telebot.TeleBot(TOKEN)

with open('dog.webp', 'rb') as photo:
    tg.send_photo(chat_id, photo)