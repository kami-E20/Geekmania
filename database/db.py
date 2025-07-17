import sqlite3
from datetime import datetime

def init_db():
    """Initialise la base de données avec les tables nécessaires"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    
    # Table utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            points INTEGER DEFAULT 0,
            badges TEXT DEFAULT 'Novice',
            last_active TIMESTAMP
        )
    ''')
    
    # Table quiz
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            user_id INTEGER,
            question TEXT,
            is_correct BOOLEAN,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Table actualités (pour le bot d'actualités)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_log (
            news_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            source TEXT,
            published_at TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_user(user_id):
    """Récupère un utilisateur"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_points(user_id, points):
    """Ajoute des points à un utilisateur"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET points = points + ? WHERE user_id = ?",
        (points, user_id)
    conn.commit()
    conn.close()
