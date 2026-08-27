name = input("Enter Student Name:")
Prn = int(input("Enter prn:"))

subject1 = int(input("Enter Marks of subject 1:"))
subject2 = int(input("Enter Marks of subject 2:"))
subject3 = int(input("Enter Marks of subject 3:"))

Total = subject1 + subject2 + subject3

Average = Total / 3

print("=============== STUDENT SCORECARD ===============")

print("Student Name :", name)
print("Prn :", Prn)

print("-----------------------------")

print("subject1 :", subject1 )
print("subject2 :", subject2 )
print("subject3 :", subject3 )

print("-----------------------------")

print(" Total Marks:", Total)
print("Average :", Average)

print("=================================================")
