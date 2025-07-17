from telegram.ext import Updater, CommandHandler
import sqlite3
import os
from datetime import datetime

# Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GROUP_ID = os.getenv("GROUP_ID")

# Connexion DB
conn = sqlite3.connect('database/geekmania.db')
cursor = conn.cursor()

def start(update, context):
    user = update.effective_user
    update.message.reply_text(
        f"🎬 Bienvenue {user.first_name} dans Geekmania !\n"
        "Utilisez /classement pour voir les tops membres."
    )

def classement(update, context):
    cursor.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT 10")
    top = cursor.fetchall()
    response = "🏆 CLASSEMENT :\n" + "\n".join(
        [f"{i+1}. {user[0]} - {user[1]} pts" for i, user in enumerate(top)]
    )
    update.message.reply_text(response)

def inviter(update, context):
    user_id = update.effective_user.id
    cursor.execute("UPDATE users SET points = points + 10 WHERE user_id = ?", (user_id,))
    conn.commit()
    update.message.reply_text("🎉 +10 points pour ton invitation !")

# Commandes principales
COMMANDS = [
    ('start', start),
    ('classement', classement),
    ('inviter', inviter),
    ('fanpass', lambda u,c: u.message.reply_text("🎭 Rôle : En cours de développement")),
    ('abodumois', lambda u,c: u.message.reply_text("📅 Abonné du mois : ...")),
    ('recompenses', lambda u,c: u.message.reply_text("🎁 Récompenses : ..."))
]

# Initialisation
updater = Updater(BOT_TOKEN)
for cmd, handler in COMMANDS:
    updater.dispatcher.add_handler(CommandHandler(cmd, handler))

updater.start_polling()