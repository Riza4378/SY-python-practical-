tasks = {
    "Assignment 1": "Pending",
    "Assignment 2": "In Progress",
    "Assignment 3": "Completed"
}

while True:
    print("\nProject Task Board")
    print("1. View Tasks")
    print("2. Update Task Status")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for task, status in tasks.items():
            print(task, ":", status)

    elif choice == "2":
        task = input("Enter task name: ")

        if task in tasks:
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")

            status = input("Enter new status (1-3): ")

            if status == "1":
                tasks[task] = "Pending"
            elif status == "2":
                tasks[task] = "In Progress"
            elif status == "3":
                tasks[task] = "Completed"
            else:
                print("Invalid status!")
                continue

            print("Task status updated successfully!")

        else:
            print("Task not found!")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
