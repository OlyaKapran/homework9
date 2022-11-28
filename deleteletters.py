from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5928697457:AAGgwvS6s-fDzU1vrMeNPEE9yE1PVVhdA-I')
updater = Updater(token='5928697457:AAGgwvS6s-fDzU1vrMeNPEE9yE1PVVhdA-I')
dispatcher = updater.dispatcher


def deletletters(update, context):
    text = update.message.text.split()
    list = []
    for i in text:
        if 'абв' not in i:
            list.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_handler = MessageHandler(Filters.text, deletletters)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
