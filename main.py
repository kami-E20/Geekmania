
import os
from flask import Flask
import telebot

# Initialisation Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Gedaj est actif sur Render 🎬"

# Initialisation du bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
bot = telebot.TeleBot(BOT_TOKEN)

# Handler de base
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

# Configuration Webhook
@app.route(f"/{BOT_TOKEN}", methods=['POST'])
def webhook():
    from flask import request
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

# Démarrage du bot via webhook
@app.before_first_request
def setup_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")

# Lancement local (optionnel)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
