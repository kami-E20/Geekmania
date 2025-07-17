from telegram.ext import Updater
from apscheduler.schedulers.background import BackgroundScheduler
import feedparser
import os

TOKEN = os.getenv("NEWS_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def send_news():
    news = feedparser.parse("https://www.allocine.fr/rss/actualites.xml")
    updater.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"📢 {news.entries[0].title}\n{news.entries[0].link}"
    )

updater = Updater(TOKEN)
scheduler = BackgroundScheduler()
scheduler.add_job(send_news, 'interval', hours=24)
scheduler.start()
updater.start_polling()
