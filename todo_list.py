# todo_list.py
import os

def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if line:
                    tasks.append(line)
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number to delete: "))
        removed = tasks.pop(n - 1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid number.")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number to mark done: "))
        # Avoid double-checkmarking
        if tasks[n-1].endswith(" ✅"):
            print("Task already marked done.")
        else:
            tasks[n-1] = tasks[n-1] + " ✅"
            print(f"Task {n} marked as done.")
    except (ValueError, IndexError):
        print("Invalid number.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

