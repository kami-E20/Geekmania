from telegram.ext import Updater, CommandHandler
import random
import os

TOKEN = os.getenv("FUN_BOT_TOKEN")
QUESTIONS = [
    {"q": "Qui a dirigé 'Avengers: Endgame' ?", "a": "Russo Brothers"}
]

def quiz(update, context):
    question = random.choice(QUESTIONS)
    update.message.reply_text(f"❓ {question['q']}")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("quiz", quiz))
updater.start_polling()
