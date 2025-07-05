import os
import telebot
from flask import Flask, request
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Gedaj est en ligne 🚀"

@app.route(f'/{BOT_TOKEN}', methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "🎬 Bienvenue sur Geekmania avec Gedaj")

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, "🤖 *Commandes disponibles : *\n"
                          "/start - Démarrer le bot\n"
                          "/help - Afficher les commandes\n"
                          "/url - Obtenir l'URL de Gedaj\n"
                          "/time - Heure actuelle\n",
                 parse_mode="Markdown")

@bot.message_handler(commands=["url"])
def url_command(message):
    bot.reply_to(message, f"L'URL publique de Gedaj est : {RENDER_URL}")

@bot.message_handler(commands=["time"])
def time_command(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot.reply_to(message, f"Heure actuelle 🕒 : {now}")

if __name__ == "__main__":
    import threading

    def run():
        bot.remove_webhook()
        bot.set_webhook(url=f"{RENDER_URL}/{BOT_TOKEN}")
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

    threading.Thread(target=run).start()
