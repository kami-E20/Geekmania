
import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "🎬 Gedaj est actif via Webhook sur Render"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Voici quelques commandes utiles :\n/start - Accueil\n/help - Aide\n/url - Lien Render du bot")

@bot.message_handler(commands=['url'])
def handle_url(message):
    bot.reply_to(message, f"🌐 Voici l'URL de Gedaj : {RENDER_URL}")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
