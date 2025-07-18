from telegram.ext import Updater
from apscheduler.schedulers.background import BackgroundScheduler
from database.db import init_db
import feedparser
import os
import logging

# Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
init_db()

def send_news():
    try:
        news = feedparser.parse("https://www.allocine.fr/rss/actualites.xml")
        if news.entries:
            updater.bot.send_message(
                chat_id=os.getenv("CHANNEL_ID"),
                text=f"📢 {news.entries[0].title}\n{news.entries[0].link}"
            )
    except Exception as e:
        logger.error(f"Erreur RSS : {e}")

if __name__ == "__main__":
    updater = Updater(os.getenv("NEWS_BOT_TOKEN"))
    
    # Planification
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_news, 'interval', hours=24)
    scheduler.start()

    updater.start_polling()
    logger.info("Bot d'actualités démarré")
    updater.idle()