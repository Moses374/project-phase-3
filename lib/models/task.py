from .config import conn, cursor
import datetime


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
        id = cursor.lastrowid
        created_at = datetime.datetime.now()  # Capture creation time explicitly
        return cls(id, title, description, False, created_at, user_id, category_id)

    @classmethod
    def find_by_id(cls, task_id):
        sql = "SELECT * FROM tasks WHERE id = ?"
        cursor.execute(sql, (task_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def mark_complete(self):
        self.completed = True
        sql = "UPDATE tasks SET completed = ? WHERE id = ?"
        cursor.execute(sql, (self.completed, self.id))
        conn.commit()

    def update(self, title=None, description=None):
        # Update only provided fields
        updates = []
        if title:
            updates.append("title = ?")
        if description:
            updates.append("description = ?")

        if updates:
            sql = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
            params = [getattr(self, field) for field in ["title", "description"] if getattr(self, field)]
            params.append(self.id)
            cursor.execute(sql, params)
            conn.commit()

