import sys
from models.user import User
from models.task import Task
from models.category import Category

def main():
    print("\nTask Manager CLI")
    while True:
        print("\n1. Task Management")
        print("2. Category Management")
        print("3. User Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_tasks()
        elif choice == '2':
            manage_categories()
        elif choice == '3':
            manage_users()
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_tasks():
    print("\n--- Task Management ---")
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Back to Main Menu")

        task_choice = input("Enter your choice: ")

        if task_choice == '1':
            add_task()
        elif task_choice == '2':
            view_tasks()
        elif task_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_task():
    print("\n--- Add Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    user_id = input("Enter user ID: ")

    try:
        task = Task.create(title=title, description=description, user_id=user_id)
        print("Task added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_tasks():
    print("\n--- View Tasks ---")
    tasks = Task.select()
    if tasks:
        for task in tasks:
            print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}, User ID: {task.user_id}")
    else:
        print("No tasks found.")

def manage_categories():
    print("\n--- Category Management ---")
    while True:
        print("\n1. Add Category")
        print("2. View Categories")
        print("3. Back to Main Menu")

        category_choice = input("Enter your choice: ")

        if category_choice == '1':
            add_category()
        elif category_choice == '2':
            view_categories()
        elif category_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_category():
    print("\n--- Add Category ---")
    name = input("Enter category name: ")

    try:
        category = Category.create(name=name)
        print("Category added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_categories():
    print("\n--- View Categories ---")
    categories = Category.select()
    if categories:
        for category in categories:
            print(f"Category ID: {category.id}, Name: {category.name}")
    else:
        print("No categories found.")

def manage_users():
    print("\n--- User Management ---")
    while True:
        print("\n1. Add User")
        print("2. View Users")
        print("3. Back to Main Menu")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            add_user()
        elif user_choice == '2':
            view_users()
        elif user_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user():
    print("\n--- Add User ---")
    username = input("Enter username: ")
    role = input("Enter role: ")

    try:
        user = User.create(username=username, role=role)
        print("User added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_users():
    print("\n--- View Users ---")
    users = User.select()
    if users:
        for user in users:
            print(f"User ID: {user.id}, Username: {user.username}, Role: {user.role}")
    else:
        print("No users found.")

if __name__ == '__main__':
    main()
