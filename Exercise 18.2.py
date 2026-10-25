filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        count = 0

        print("\n--- LOG FILE CONTENTS ---")

        for line in file:
            print(line, end="")
            count += 1

        print("\n\nTotal number of lines:", count)

except FileNotFoundError:
    print("File not found!")
