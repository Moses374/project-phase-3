# File: __init__.py
from models.task import Task
from models.user import User
from models.category import Category

# Create tables
Task.create_table()
User.create_table()
Category.create_table()

print("Tables created successfully.")


