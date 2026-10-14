Student = {}

while True:
    print("1. Store Student Contact")
    print("2. Search Student Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))
    print("-----------------------------------")

    if choice == 1:
        Roll_No = int(input("Enter Student Roll No: "))
        Email = input("Enter Student Email: ")

        Student[Roll_No] = Email
        print(Student)
        print("Student Contact Added Successfully.")
        print("-----------------------------------")

    elif choice == 2:
        Roll_No = int(input("Enter Student Roll No: "))

        if Roll_No in Student:
            print("Student Email:", Student[Roll_No])
        else:
            print("Student Roll No Not Found.")

    elif choice == 3:
        print("Student Contact Database:")
        print(Student)
        print("-----------------------------------")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
