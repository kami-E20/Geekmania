from telegram.ext import Updater, CommandHandler
from database.db import init_db, update_points, get_user
import random
import os

init_db()
BOT_TOKEN = os.getenv("FUN_BOT_TOKEN")

QUESTIONS = [
    {"q": "Qui a réalisé 'Inception' ?", "a": "Christopher Nolan"},
    {"q": "Quel studio anime 'Attack on Titan' ?", "a": "Wit Studio"}
]

def quiz(update, context):
    question = random.choice(QUESTIONS)
    context.user_data['current_question'] = question
    update.message.reply_text(f"❓ {question['q']}\nRéponds avec /reponse [ta_réponse]")

def reponse(update, context):
    user_answer = ' '.join(context.args).strip().lower()
    correct_answer = context.user_data.get('current_question', {}).get('a', '').lower()
    
    if user_answer == correct_answer:
        update_points(update.effective_user.id, 5)
        update.message.reply_text("✅ Correct ! +5 points")
    else:
        update.message.reply_text(f"❌ Faux ! La réponse était : {correct_answer}")

COMMANDS = [
    ('quiz', quiz),
    ('reponse', reponse),
    ('correction', lambda u,c: u.message.reply_text("📖 Correction : ...")),
    ('avis', lambda u,c: u.message.reply_text("❤️ Donne ton avis ici : ...")),
    ('defi', lambda u,c: u.message.reply_text("🎯 Défi : Nommez 3 films de Nolan !"))
]

updater = Updater(BOT_TOKEN)
for cmd, handler in COMMANDS:
    updater.dispatcher.add_handler(CommandHandler(cmd, handler))

updater.start_polling()