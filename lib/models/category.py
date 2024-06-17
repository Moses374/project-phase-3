from .config import conn, cursor


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

    @classmethod
    def find_by_id(cls, category_id):
        sql = "SELECT * FROM categories WHERE id = ?"
        cursor.execute(sql, (category_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM categories WHERE name = ?"
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def update(self, new_name):
        if new_name != self.name:
            sql = "UPDATE categories SET name = ? WHERE id = ?"
            cursor.execute(sql, (new_name, self.id))
            conn.commit()
            self.name = new_name

