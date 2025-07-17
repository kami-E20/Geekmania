from telegram.ext import Updater, CommandHandler
from database.db import init_db, get_leaderboard
import os

init_db()
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🎬 Bienvenue sur GeekmaniaOfficiel !")

def classement(update, context):
    leaderboard = get_leaderboard()
    response = "🏆 Classement :\n" + "\n".join(
        f"{idx+1}. {user[0]} - {user[1]} pts" 
        for idx, user in enumerate(leaderboard)
    )
    update.message.reply_text(response)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("classement", classement))
updater.start_polling()
