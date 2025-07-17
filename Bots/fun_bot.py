from telegram.ext import Updater, CommandHandler
import random
import os

BOT_TOKEN = os.getenv("FUN_BOT_TOKEN")

# Quiz System
QUESTIONS = [
    {"q": "Qui a réalisé 'Inception' ?", "a": "Christopher Nolan"},
    {"q": "Quel studio anime 'One Piece' ?", "a": "Toei Animation"}
]

def quiz(update, context):
    question = random.choice(QUESTIONS)
    context.user_data['answer'] = question['a']
    update.message.reply_text(f"❓ {question['q']}\nRéponds avec /reponse [ta_réponse]")

def correction(update, context):
    update.message.reply_text(f"📖 Correction : {context.user_data.get('answer', 'Aucune question en cours')}")

def avis(update, context):
    update.message.reply_text("❤️ Donne ton avis ici : https://forms.gle/...")

COMMANDS = [
    ('quiz', quiz),
    ('correction', correction),
    ('avis', avis),
    ('suggestion', lambda u,c: u.message.reply_text("💡 Propose un contenu via /suggestion [titre]")),
    ('translate', lambda u,c: u.message.reply_text("🌐 Traduction : En développement")),
    ('lang', lambda u,c: u.message.reply_text("🗣️ Langues disponibles : FR/EN")),
    ('vision', lambda u,c: u.message.reply_text("👓 Préférences : Films/Séries/Manga")),
    ('defi', lambda u,c: u.message.reply_text("🎯 Défi : Nommez 3 films de Miyazaki !"))
]

updater = Updater(BOT_TOKEN)
for cmd, handler in COMMANDS:
    updater.dispatcher.add_handler(CommandHandler(cmd, handler))

updater.start_polling()
