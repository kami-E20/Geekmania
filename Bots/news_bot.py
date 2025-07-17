from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
import feedparser
import os

BOT_TOKEN = os.getenv("NEWS_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def filmdujour(update, context):
    films = ["Dune 2", "Spider-Verse", "Oppenheimer"]
    update.message.reply_text(f"🎬 Film du jour : {films[datetime.now().weekday() % 3]}")

def prochainfilm(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔭 Prochainement :\n- Deadpool 3\n- Joker 2"
    )

# Actualités automatisées
def send_news():
    news = feedparser.parse("https://www.allocine.fr/rss/actualites.xml")
    updater.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"📢 {news.entries[0].title}\n{news.entries[0].link}"
    )

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('filmdujour', filmdujour))
updater.dispatcher.add_handler(CommandHandler('prochainfilm', prochainfilm))
updater.dispatcher.add_handler(CommandHandler('source', lambda u,c: u.message.reply_text("📚 Sources : AlloCiné, IMDb")))
updater.dispatcher.add_handler(CommandHandler('spoiler', lambda u,c: u.message.reply_text("🔐 Mode anti-spoiler activé !")))

scheduler = BackgroundScheduler()
scheduler.add_job(send_news, 'interval', hours=24)
scheduler.start()

updater.start_polling()
