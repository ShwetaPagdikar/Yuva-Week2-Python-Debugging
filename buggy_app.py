
def main():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == 1:
            task = input("Enter task: ")
            tasks.append(task)

        elif choice == "2":
            for i in range(len(tasks) + 1):
                print(i + 1, tasks[i])

        elif choice == "3":
            index = int(input("Enter task number: "))
            tasks.pop(index)

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
