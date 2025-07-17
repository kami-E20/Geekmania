import sqlite3
from datetime import datetime

def init_db():
    """Initialise la base de données avec les tables"""
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
            quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            question TEXT,
            is_correct BOOLEAN,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
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
    return user or None

def add_user(user_id, username):
    """Ajoute un nouvel utilisateur"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, username, last_active) VALUES (?, ?, ?)",
        (user_id, username, datetime.now())
    )
    conn.commit()
    conn.close()

def update_points(user_id, points):
    """Met à jour les points d'un utilisateur"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET points = points + ?, last_active = ? WHERE user_id = ?",
        (points, datetime.now(), user_id)
    )
    conn.commit()
    conn.close()

def get_leaderboard(limit=10):
    """Récupère le classement"""
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, points FROM users ORDER BY points DESC LIMIT ?",
        (limit,)
    )
    leaderboard = cursor.fetchall()
    conn.close()
    return leaderboard