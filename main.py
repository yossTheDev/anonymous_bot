from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, updater
import os
import logging
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Keys
TOKEN = os.environ['TOKEN']
PORT = int(os.environ.get('PORT', '8443'))

# Bot Messages
help_message = """Is very easy to use :
        
➡ Add me as an administrator to a group               
➡ Give me permission to delete messages
➡ And see the magic 🎈🎈"""
about_message = """It was created by :     
[Yoss THE DEV](https://t.me/yossthedev)

[GitHub](https://github.com/yossTheDev/anonymous_bot)"""
welcome_message = """
I can help you to return all the
messages of your group in anonymous messages 🤫
 
press /help to see how to use it
press /about to learn about me"""

def test(update: Update, context: CallbackContext) -> None:
        update.message.reply_text(requests.get('https://uvs.ucm.cmw.sld.cu/ ').url)

def main():
    # Method to answer messages from users
    def echo(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

    # Welcome Message
    def start(update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Hello" + update.effective_user.first_name + welcome_message)

    # Help Message
    def help(update: Update, context: CallbackContext) -> None:
        update.message.reply_text(help_message)

    # About Message
    def about(update: Update, context: CallbackContext) -> None:
        update.message.reply_text(about_message)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    updater = Updater(os.environ['TOKEN'])

    # Add command handlers
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('test', test))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('about', about))
    updater.dispatcher.add_handler(echo_handler)

    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://anonymous4everbot.herokuapp.com/" + TOKEN)
    updater.idle()
# g
main()
