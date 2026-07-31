print("============ Monthly Expense Tracker =============")

n=int(input("Enter the number of expenses:"))
expenses = []
total=0

for i in range(n):
    amount = float(input(f"Enter expenses {i+1}:"))
    
    expenses.append(amount)
    total+=amount
    
while True:
    print("\n======= Expense Tracker menu =======")    
    print("1. show all expenses")
    print("2. show total of expenses")
    print("3. add new expenses")
    print("4. exit")
    choice = int(input("enter your choice:"))
    
    if choice == 1:
        print("\n expense list:")
        for i in range(len(expenses)):
            print(f"expense {i+1}: {expenses [i] }")
            
    elif choice == 2:
        print("total monthly expense =",total)   
            
    elif choice == 3:
        new_expense = float(input("enter new expense:"))    
        expenses.append(new_expense)
        total += new_expense
        print("expense added successfully!!")
        
    elif choice == 4:
        print("thank you for using the our monthly expense tracker !!") 
           
        break
    else:
        print("Invalid choice!! please try again. ")


