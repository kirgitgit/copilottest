import sqlite3
from db_config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)
# DB_PATH = DB_PATH = '/path/to/your/database.db'

def create_users_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        conn.commit()

def insert_users(users_data):
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = '''INSERT INTO users (name, email) VALUES (?, ?)'''
        cursor.executemany(sql, users_data)
        conn.commit()

def fetch_all_users():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
