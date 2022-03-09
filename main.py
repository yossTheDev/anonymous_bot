from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    context.bot.delete_message(chat_id=update.effective_chat.id,message_id=update.message.message_id)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

updater = Updater('5211534226:AAFd0VBARRIpGOqmFs1Agg0x7h0HBAajkUw')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(echo_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path="5211534226:AAFd0VBARRIpGOqmFs1Agg0x7h0HBAajkUw")

updater.bot.setWebhook('https://anonymous4everbot.herokuapp.com/' + "5211534226:AAFd0VBARRIpGOqmFs1Agg0x7h0HBAajkUw")

updater.idle()
