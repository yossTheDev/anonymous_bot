from telegram import Update
from telegram.ext import Updater , CommandHandler , CallbackContext

about_message = """It was created by :     
[Yoss THE DEV](https://t.me/yossthedev)

[GitHub](https://github.com/yossTheDev/anonymous_bot)"""

# About Message
def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(about_message)
    
updater = Updater ( os.envirom["TOKEN"])
updater.dispatcher.add_handler (CommandHandler( 'hello' , hello ))
updater.start_polling ()
updater.idle()
  