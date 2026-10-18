
from pathlib import Path


def add_task(tasks, title):
    """Add a task after validating its title."""
    title = title.strip()

    if not title:
        raise ValueError("Task cannot be empty.")

    tasks.append(title)


def remove_task(tasks, task_number):
    """Remove a task using its displayed number."""
    if not isinstance(task_number, int):
        raise ValueError("Task number must be an integer.")

    if task_number < 1 or task_number > len(tasks):
        raise ValueError("Invalid task number.")

    return tasks.pop(task_number - 1)


def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with Path(filename).open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks(filename):
    """Load tasks from a file if it exists."""
    path = Path(filename)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def display_tasks(tasks):
    """Display tasks with numbers starting at 1."""
    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Save and exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter task: ")

            try:
                add_task(tasks, title)
                print("Task added successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            display_tasks(tasks)

            if not tasks:
                continue

            try:
                number = int(
                    input("Enter task number to remove: ")
                )
                removed = remove_task(tasks, number)
                print(f"Removed task: {removed}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            display_tasks(tasks)

        elif choice == "4":
            save_tasks(tasks, filename)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
