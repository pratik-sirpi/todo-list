import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Loads tasks from the todo file if it exists."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(todo_list):
    """Saves the current list of tasks to the file."""
    with open(TODO_FILE, "w") as f:
        for task in todo_list:
            f.write(f"{task}\n")

def main():
    todo_list = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Sort Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            if not todo_list:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(todo_list):
                    print(f"{idx + 1}. {task}")
        elif choice == '2':
            task = input("Enter the task to add: ")
            todo_list.append(task)
            save_tasks(todo_list)
            print(f"Task '{task}' added successfully!")
        elif choice == '3':
            if not todo_list:
                print("Your to-do list is empty. Nothing to delete.")
                continue
            
            print("\nCurrent Tasks:")
            for idx, task in enumerate(todo_list):
                print(f"{idx + 1}. {task}")
            
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_index < len(todo_list):
                    deleted_task = todo_list.pop(task_index)
                    save_tasks(todo_list)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.sort()
            save_tasks(todo_list)
            print("Tasks sorted alphabetically!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
