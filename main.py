import os
import logging
from telegram.ext import Updater, CommandHandler

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("🚀 Bot opérationnel avec Python 3.9 et PTB 13.7 !")

def error_handler(update, context):
    logger.error(f"Erreur : {context.error}")

def main():
    try:
        # Initialisation
        updater = Updater(os.getenv("BOT_TOKEN"))
        
        # Commandes
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_error_handler(error_handler)

        # Lancement
        updater.start_polling()
        logger.info("Bot démarré avec succès")
        updater.idle()
        
    except Exception as e:
        logger.critical(f"Échec du démarrage : {e}")

if __name__ == "__main__":
    main()