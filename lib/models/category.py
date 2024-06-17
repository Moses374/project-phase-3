from .config import conn, cursor
import sqlite3

# Database initialization
DATABASE_NAME = 'task_manager.db'
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()


class Category:
   def __init__(self, id, name):
       self.id = id
       self.name = name

   @classmethod
   def create_table(cls):
       cursor.execute("""
           CREATE TABLE IF NOT EXISTS categories (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT
           )
       """)
       conn.commit()

   @classmethod
   def create(cls, name):
       cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
       conn.commit()
       return cls(cursor.lastrowid, name)
