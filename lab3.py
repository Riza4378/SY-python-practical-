print("---------- College Admission Eligiblity Checker----------")

num_age = int(input("enter age :"))
num_marks = float(input("enter marks :"))

if num_age >17 and num_age<25:
    print("you are eligible for admission")
    if num_marks>=60:
        if num_marks>80:
            print("you are is eligible to AIML department")
        elif num_marks<80:
            print("you are is eligible to CSE  department")
        elif num_marks<70:
            print("you are eligible to MECHANICAL department ")       
    else :
        print(" you are is not eligible because of marks")    
else:
    print("you are not eligible to admission  because of age") 

 
