import sqlite3

# Database initialization
DATABASE_NAME = 'task_manager.db'
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()


class Task:
    def __init__(self, id, title, description, completed, created_at, user_id, category_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at
        self.user_id = user_id
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        """)
        conn.commit()

    @classmethod
    def create(cls, title, description, user_id, category_id=None):
        cursor.execute("INSERT INTO tasks (title, description, user_id, category_id) VALUES (?, ?, ?, ?)",
                       (title, description, user_id, category_id))
        conn.commit()
        return cls(cursor.lastrowid, title, description, False, None, user_id, category_id)
