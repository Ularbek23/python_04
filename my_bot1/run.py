from Calambur import TelegramBot
token = "6935378517:AAF3ay_KYtIWKVvrBRpW1EthWNz5bWp2xJo"
bot = TelegramBot(token)
stiker = "CAACAgIAAxkBAAJRomU3qaWpQbuatdNEMi83i-HUAAENXgACCQADjKp7NPZWG_Ad14k8MAQ"
chat_id = 1020812876
# bot.send_message(chat_id, "🐭")
# print(bot.get_updates())

bot.sync_chats()
bot.spam("test Ularbek")
bot.create_excel_chats()
bot.get_chats_excel()
# bot.get_sticker(chat_id, stiker)