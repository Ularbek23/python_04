from tg_bot import TelegramBot
token = "6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0"
bot = TelegramBot(token)

chat_id = "270623373"
# bot.send_message(chat_id, "Ularbek")

bot.sync_chats()
bot.spam("test Ularbek")