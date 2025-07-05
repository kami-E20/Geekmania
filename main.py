import os
import telebot
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    return "Gedaj est actif sur Render 🚀"

# Webhook setup
bot.remove_webhook()
bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")

# Handlers
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "📌 Commandes disponibles : /start /help /url")

@bot.message_handler(commands=['url'])
def handle_url(message):
    if str(message.from_user.id) == str(ADMIN_ID):
        bot.reply_to(message, f"L'URL de Gedaj est : {RENDER_URL}")
    else:
        bot.reply_to(message, "⛔ Désolé, cette commande est réservée à l'admin.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))