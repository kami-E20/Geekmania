
import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "🎬 Gedaj est actif sur Render (Webhook activé)"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Voici quelques commandes utiles :\n/start - Accueil\n/help - Aide\n/url - Lien Render du bot")

@bot.message_handler(commands=['url'])
def url_command(message):
    bot.reply_to(message, f"🌐 Voici l'URL de Gedaj : {RENDER_URL}")

if __name__ == '__main__':
    print("🚀 Activation du webhook...")
    bot.remove_webhook()
    webhook_set = bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")
    print("✅ Webhook configuré :", webhook_set)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
