from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def main():
    updater = Updater("351428863:AAGr6X6lZkSFRPNX5CiX_8fVKuf5gmxeD4o")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler((Filters.text | Filters.venue) & Filters.forwarded, talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()
def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)
def show_error(bot, update, error):
    print(error)
main()
