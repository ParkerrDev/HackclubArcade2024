import sys

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(index):
    try:
        task = tasks.pop(index - 1)
        print(f"Removed task: {task}")
    except IndexError:
        print("Invalid task number")

def main():
    while True:
        command = input("Enter a command (add, remove, show, quit): ").strip().lower()
        if command == "add":
            task = input("Enter a task: ").strip()
            add_task(task)
        elif command == "remove":
            try:
                index = int(input("Enter task number to remove: ").strip())
                remove_task(index)
            except ValueError:
                print("Please enter a valid number")
        elif command == "show":
            show_tasks()
        elif command == "quit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
