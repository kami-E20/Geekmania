from telegram.ext import Updater, CommandHandler
from database.db import init_db, get_leaderboard
import os
import logging

# Config logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Init DB
init_db()

def start(update, context):
    """Gère la commande /start"""
    user = update.effective_user
    update.message.reply_text(f"🎬 Bienvenue {user.first_name} sur GeekmaniaOfficiel !")

def classement(update, context):
    """Gère la commande /classement"""
    leaderboard = get_leaderboard()
    response = "🏆 Classement :\n" + "\n".join(
        f"{i+1}. {user[0]} - {user[1]} pts" for i, user in enumerate(leaderboard)
    )
    update.message.reply_text(response)

def error_handler(update, context):
    """Gère les erreurs"""
    logger.error(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    updater = Updater(os.getenv("BOT_TOKEN"))
    dp = updater.dispatcher

    # Commandes
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("classement", classement))

    # Gestion erreurs
    dp.add_error_handler(error_handler)

    # Lancement
    updater.start_polling()
    logger.info("Bot principal démarré")
    updater.idle()