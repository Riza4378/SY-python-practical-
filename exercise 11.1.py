Theatre = [["O", "O", "O"],
           ["O", "O", "O"],
           ["O", "O", "O"]]

print("--------MOVIE THEATRE SEAT RESERVATION--------")

for i in range(3):
    print(Theatre[i])

print("\n**** Please select your seat ****")

row = int(input("Enter your row number: "))
seat = int(input("Enter your seat number: "))

if Theatre[row-1][seat-1] == "O":
    Theatre[row-1][seat-1] = "X"
    print("Your seat is reserved..!")
    print("--------------------------------")
else:
    print("Seat is already reserved..!")

print("\nUpdated Seat Arrangement:")

for i in range(3):
    print(Theatre[i])
