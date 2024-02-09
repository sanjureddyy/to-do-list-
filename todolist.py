import json
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['date']}")

def add_task(tasks, title):
    new_task = {'title': title, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':            show_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '3':
            show_tasks(tasks)
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")

if __name__ == "__main__":
    main()
