import sys
from datetime import datetime
from models.user import User
from models.task import Task
from models.category import Category

def main():
    while True:
        print("\nTask Manager CLI")
        print("1. Task Management")
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
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_tasks():
    while True:
        print("\nTask Management")
        print("1. Add Task")
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
    # Your code to add a task
    pass

def view_tasks():
    # Your code to view tasks
    pass

def manage_categories():
    while True:
        print("\nCategory Management")
        print("1. Add Category")
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
    # Your code to add a category
    pass

def view_categories():
    # Your code to view categories
    pass

def manage_users():
    while True:
        print("\nUser Management")
        print("1. Add User")
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
    # Your code to add a user
    pass

def view_users():
    # Your code to view users
    pass

if __name__ == '__main__':
    main()
