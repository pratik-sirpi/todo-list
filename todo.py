import os
import sys

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines() if line.strip()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: '{task}'")

def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        deleted = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: '{deleted}'")
    else:
        print("Invalid task number.")

def sort_tasks():
    tasks = load_tasks()
    tasks.sort()
    save_tasks(tasks)
    print("Tasks sorted alphabetically.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def print_help():
    print("To-Do List Commands:")
    print("  python todo.py add <task description>  - Add a new task")
    print("  python todo.py list                    - List all tasks")
    print("  python todo.py delete <task number>    - Delete a task by number")
    print("  python todo.py sort                    - Sort tasks alphabetically")
    print("  python todo.py help                    - Show this help message")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_tasks()
        print("\nType 'python todo.py help' for usage instructions.")
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            print("Usage: python todo.py add <task description>")
        else:
            task = " ".join(sys.argv[2:])
            add_task(task)
    elif command == "list":
        list_tasks()
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task number.")
            print("Usage: python todo.py delete <task number>")
        else:
            try:
                index = int(sys.argv[2])
                delete_task(index)
            except ValueError:
                print("Error: Task number must be an integer.")
    elif command == "sort":
        sort_tasks()
    elif command in ("help", "-h", "--help"):
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()
