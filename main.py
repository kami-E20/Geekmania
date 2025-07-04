import os
import telebot
from threading import Thread
from web import run_web

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
ADMIN_IDS = [879386491, 5618445554]

bot = telebot.TeleBot(BOT_TOKEN)

# Commande /start
@bot.message_handler(commands=['start'])
def start_cmd(msg):
    bot.reply_to(msg, "🎬 Bienvenue sur *Geekmania* avec Gedaj !", parse_mode="Markdown")

# Commande /help
@bot.message_handler(commands=['help'])
def help_cmd(msg):
    bot.reply_to(msg, "📘 Voici ce que je peux faire pour toi :
"
                      "• /call – M’appeler si besoin
"
                      "• /help – Afficher cette aide
"
                      "• /abodumois – Voir comment devenir abonné du mois
"
                      "• /url – Obtenir l'URL de mon serveur
"
                      "• Tape GEDAJ dans le groupe pour me faire réagir 😉")

# Commande /url (admin uniquement)
@bot.message_handler(commands=['url'])
def send_url(msg):
    if msg.from_user.id in ADMIN_IDS:
        bot.reply_to(msg, f"🌍 Mon URL Render : {RENDER_URL}")
    else:
        bot.reply_to(msg, "⛔ Désolé, tu n’es pas autorisé à voir cette info.")

# Commande /call
@bot.message_handler(commands=['call'])
def call_cmd(msg):
    if msg.from_user.id == 879386491:
        bot.reply_to(msg, "👋 Oui papa, je t’écoute.")
    elif msg.from_user.id == 5618445554:
        bot.reply_to(msg, "👋 Oui tonton, je suis là.")
    else:
        bot.reply_to(msg, "✅ Je suis bien présent, tape /help pour voir ce que je fais.")

# Commande /abodumois
@bot.message_handler(commands=['abodumois'])
def abo_mois_cmd(msg):
    bot.reply_to(msg,
        "🏆 *Abonné du Mois - Geekmania*

"
        "Les *5 meilleurs abonnés* du mois reçoivent un *cadeau spécial signé Geekmania* !

"
        "✅ Comment être éligible ?
"
        "• Réagir aux publications (❤️ 👍 etc.)
"
        "• Participer aux quiz, commentaires, défis
"
        "• Gagner le badge d’abonné hebdomadaire plusieurs fois
"
        "• Inviter de nouveaux abonnés dans le groupe ou canal

"
        "🎁 Les gagnants recevront leurs cadeaux dans le groupe VIP. Continue de participer et monte dans le classement !

"
        "_Continue à interagir chaque jour, et tu seras peut-être l’heureux élu !_", parse_mode="Markdown")

# Réactions à "GEDAJ"
@bot.message_handler(func=lambda m: m.text and 'gedaj' in m.text.lower())
def react_gedaj(msg):
    uid = msg.from_user.id
    if uid == 879386491:
        bot.reply_to(msg, "👑 Oui papa !")
    elif uid == 5618445554:
        bot.reply_to(msg, "👑 Oui tonton !")
    else:
        bot.reply_to(msg, "🤖 Je suis là, n’hésite pas à taper /help")

# Lancer le bot et l'interface web
if __name__ == "__main__":
    Thread(target=run_web).start()
    bot.infinity_polling()