"""
DecodeLabs - Python Programming | Project 1: The To-Do List

Concepts covered (from the project brief):
  * Lists          -> my_tasks = []  and  my_tasks.append(...)
  * Print loops    -> for ... in enumerate(my_tasks, start=1)
  * Dictionaries   -> each task is a "row": {"id": 1, "task": "Code", ...}
  * IPO model      -> Input (menu) -> Process (add/complete/delete) -> Output (display)
  * Decoupling     -> MODEL (data logic) is separate from VIEW (user interface)
  * Persistence    -> tasks are saved to tasks.json so RAM loss doesn't lose data
  * Entry point    -> if __name__ == "__main__": main()
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


# ======================================================================
# MODEL  (Data logic - no input() or print() here)
# ======================================================================
def load_tasks(path=DATA_FILE):
    """Read tasks from disk. Return an empty list if the file is missing/corrupt."""
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks, path=DATA_FILE):
    """Serialize the list of task dictionaries to JSON (RAM -> Disk)."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def next_id(tasks):
    """Primary-key style ID: one more than the highest existing ID."""
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(tasks, title):
    """Create a task dictionary and append it to the list."""
    title = title.strip()
    if not title:
        raise ValueError("Task cannot be empty.")
    task = {"id": next_id(tasks), "task": title, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, position):
    """Mark the task at a 1-based position as done."""
    task = tasks[_to_index(tasks, position)]
    task["done"] = True
    return task


def delete_task(tasks, position):
    """Remove the task at a 1-based position and return it."""
    return tasks.pop(_to_index(tasks, position))


def _to_index(tasks, position):
    """Convert a 1-based position to a list index, validating the range."""
    if not 1 <= position <= len(tasks):
        raise IndexError(f"Choose a number between 1 and {len(tasks)}.")
    return position - 1


# ======================================================================
# VIEW  (User interface - all input() and print() lives here)
# ======================================================================
def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def display_tasks(tasks):
    """The READ operation: loop over the list with enumerate()."""
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"  {number}. {status} {task['task']}")


def ask_position(prompt):
    """Ask for a task number; return None if the input isn't a number."""
    raw = input(prompt).strip()
    if not raw.isdigit():
        print("Please enter a valid number.")
        return None
    return int(raw)


# ======================================================================
# CONTROLLER  (ties Input -> Process -> Output together)
# ======================================================================
def main():
    my_tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter a new task: ")
            try:
                task = add_task(my_tasks, title)
                save_tasks(my_tasks)
                print(f"Added: {task['task']}")
            except ValueError as error:
                print(error)

        elif choice == "2":
            display_tasks(my_tasks)

        elif choice == "3":
            display_tasks(my_tasks)
            if my_tasks:
                position = ask_position("Task number to mark as done: ")
                if position is not None:
                    try:
                        task = complete_task(my_tasks, position)
                        save_tasks(my_tasks)
                        print(f"Completed: {task['task']}")
                    except IndexError as error:
                        print(error)

        elif choice == "4":
            display_tasks(my_tasks)
            if my_tasks:
                position = ask_position("Task number to delete: ")
                if position is not None:
                    try:
                        task = delete_task(my_tasks, position)
                        save_tasks(my_tasks)
                        print(f"Deleted: {task['task']}")
                    except IndexError as error:
                        print(error)

        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
