from telegram import *
from telegram.ext import *

bot = Bot("token")
print(bot.get_me())

updater = Updater("token", use_context=True)

dispatcher = updater.dispatcher
# For Commands
def test_fnc2(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welkom bij mijn Haikus ",
    )


start_value2 = CommandHandler("start", test_fnc2)
dispatcher.add_handler(start_value2)

# adding more Command
def test_fnc(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Haiku link: https://www.henkvanderduim.nl/hersenspinsels/haiku/ ",
    )


start_value = CommandHandler("python", test_fnc)
dispatcher.add_handler(start_value)

updater.start_polling()
