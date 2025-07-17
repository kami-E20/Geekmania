from telegram.ext import Updater, CommandHandler
from database.db import init_db, add_user, update_points, get_leaderboard
import os

# Initialisation
init_db()
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    user = update.effective_user
    add_user(user.id, user.username)
    update.message.reply_text(
        f"🎬 Bienvenue {user.first_name} !\n"
        "Utilisez /classement pour voir les tops membres."
    )

def classement(update, context):
    leaderboard = get_leaderboard()
    response = "🏆 CLASSEMENT :\n" + "\n".join(
        [f"{i+1}. {user[0]} - {user[1]} pts" for i, user in enumerate(leaderboard)]
    )
    update.message.reply_text(response)

def inviter(update, context):
    update_points(update.effective_user.id, 10)
    update.message.reply_text("🎉 +10 points pour ton invitation !")

COMMANDS = [
    ('start', start),
    ('classement', classement),
    ('inviter', inviter),
    ('fanpass', lambda u,c: u.message.reply_text("🎭 Rôle : Fan certifié")),
    ('abodumois', lambda u,c: u.message.reply_text("📅 Abonné du mois : ...")),
    ('recompenses', lambda u,c: u.message.reply_text("🎁 Récompenses : Bientôt disponible !"))
]

updater = Updater(BOT_TOKEN)
for cmd, handler in COMMANDS:
    updater.dispatcher.add_handler(CommandHandler(cmd, handler))

updater.start_polling()