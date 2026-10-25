while True:
    print("\n--- PERSONAL DIARY SYSTEM ---")
    print("1. Add Diary Entry")
    print("2. Display All Entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        thought = input("Write your thoughts: ")

        with open("diary.txt", "a") as file:
            file.write(thought + "\n\n")

        print("Diary entry saved successfully!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                entries = file.read()

                if entries:
                    print("\n--- ALL DIARY ENTRIES ---")
                    print(entries)
                else:
                    print("No diary entries found.")

        except FileNotFoundError:
            print("Diary file does not exist yet.")

    elif choice == "3":
        print("Exiting Personal Diary System.")
        break

    else:
        print("Invalid choice. Please try again.")
