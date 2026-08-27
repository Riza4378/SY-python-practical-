print("********Student Scholership Eligibility System******** ")

age = int(input("Enter your age:"))
income = float(input("Enter your income:"))
cast = input("Enter your caste: ").upper()


if age < 25 and income <300000  and cast in ["SC","ST","OBC"]:
    print(" Congratulation ! you are qualify for the scholarship scheme.")

else:
    print("sorry ! you are not qualify for the scholarship scheme.  ")