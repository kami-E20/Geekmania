from telegram.ext import Updater, CommandHandler
from database.db import init_db, update_points
import random
import os
import logging

# Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
init_db()

QUESTIONS = [
    {"q": "Qui a réalisé 'Inception' ?", "a": "Christopher Nolan"},
    {"q": "Quel studio anime 'Attack on Titan' ?", "a": "Wit Studio"}
]

def quiz(update, context):
    """Gère /quiz"""
    question = random.choice(QUESTIONS)
    context.user_data['current_question'] = question
    update.message.reply_text(f"❓ {question['q']}\nRéponds avec /reponse [ta_réponse]")

def reponse(update, context):
    """Gère /reponse"""
    user_answer = ' '.join(context.args).lower()
    correct_answer = context.user_data.get('current_question', {}).get('a', '').lower()
    
    if user_answer == correct_answer:
        update_points(update.effective_user.id, 5)
        update.message.reply_text("✅ Correct ! +5 points")
    else:
        update.message.reply_text(f"❌ Faux ! Réponse : {correct_answer.capitalize()}")

if __name__ == "__main__":
    updater = Updater(os.getenv("FUN_BOT_TOKEN"))
    dp = updater.dispatcher

    # Commandes
    dp.add_handler(CommandHandler("quiz", quiz))
    dp.add_handler(CommandHandler("reponse", reponse))

    updater.start_polling()
    logger.info("Bot de jeux démarré")
    updater.idle()