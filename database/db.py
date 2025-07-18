import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'users.db')

def init_db():
    """Initialise la base de données"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            points INTEGER DEFAULT 0,
            last_active TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def update_points(user_id, points):
    """Ajoute des points"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET points = points + ?, last_active = ? WHERE user_id = ?",
        (points, datetime.now(), user_id)
    )
    conn.commit()
    conn.close()

def get_leaderboard(limit=10):
    """Récupère le classement"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, points FROM users ORDER BY points DESC LIMIT ?",
        (limit,)
    )
    leaderboard = cursor.fetchall()
    conn.close()
    return leaderboard