import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
ADMIN_ID = os.getenv("ADMIN_ID")
SECOND_ADMIN_ID = os.getenv("SECOND_ADMIN_ID")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Gedaj est actif 🚀"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, (
        "🤖 *Commandes disponibles :*

"
        "/start – Lancer le bot
"
        "/help – Obtenir la liste des commandes
"
        "/url – Obtenir l'URL du bot Render
"
        "/test – Vérifier si tout fonctionne bien
"
    ), parse_mode='Markdown')

@bot.message_handler(commands=['url'])
def handle_url(message):
    bot.reply_to(message, f"🌐 URL Render : {RENDER_URL}")

@bot.message_handler(commands=['test'])
def handle_test(message):
    if str(message.from_user.id) in [ADMIN_ID, SECOND_ADMIN_ID]:
        bot.reply_to(message, "✅ Le bot fonctionne correctement et vous êtes un admin !")
    else:
        bot.reply_to(message, "❌ Vous n'avez pas accès à cette commande.")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))