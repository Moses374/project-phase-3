# File: config.py
import sqlite3

# Database initialization
DATABASE_NAME = 'task_manager.db'
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
