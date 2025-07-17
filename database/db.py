import sqlite3
from datetime import datetime
import os

# Chemin absolu pour Render
DB_PATH = os.path.join(os.path.dirname(__file__), 'users.db')

def init_db():
    """Initialise la base de données"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            points INTEGER DEFAULT 0,
            badges TEXT DEFAULT 'Novice',
            last_active TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT 10")
    leaderboard = cursor.fetchall()
    conn.close()
    return leaderboard
