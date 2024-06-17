import sqlite3

# Database initialization
DATABASE_NAME = 'task_manager.db'
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()


class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

    @classmethod
    def create_table(cls):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                role TEXT
            )
        """)
        conn.commit()

    @classmethod
    def create(cls, username, role):
        cursor.execute("INSERT INTO users (username, role) VALUES (?, ?)", (username, role))
        conn.commit()
        return cls(cursor.lastrowid, username, role)

    @classmethod
    def find_by_id(cls, user_id):
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def find_by_username(cls, username):
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def all(cls):
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def update(self, username=None, role=None):
        if username:
            self.username = username
        if role:
            self.role = role
        cursor.execute("UPDATE users SET username = ?, role = ? WHERE id = ?", (self.username, self.role, self.id))
        conn.commit()


    def delete(self):
        cursor.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
