Schedule = [
    ["Maths", "English", "Physics", "Chemistry", "Python"],
    ["English", "Maths", "Python", "Physics", "Chemistry"],
    ["Physics", "Python", "Maths", "English", "Maths"]
]

print("-------- CLASS SCHEDULE --------")

for i in range(3):
    print(Schedule[i])

print("\n**** Please select your class ****")

row = int(input("Enter hour number: "))
day = int(input("Enter day number: "))

print("Current subject:", Schedule[row-1][day-1])

subject = input("Enter new subject: ")

Schedule[row-1][day-1] = subject

print("Subject updated successfully..!")

print("\n-------- UPDATED SCHEDULE --------")

for i in range(3):
    print(Schedule[i])
