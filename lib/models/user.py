from .config import conn, cursor
import sqlite3

# Database initialization
DATABASE_NAME = 'task_manager.db'
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @classmethod
    def create_table(cls):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT
            )
        """)
        conn.commit()

    @classmethod
    def create(cls, username):
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        return cls(cursor.lastrowid, username)
