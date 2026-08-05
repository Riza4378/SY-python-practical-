print("============ Monthly Expense Tracker =============")
food=0
travel=0
shopping=0
total=0
others=0

while True:
    value=float(input("Enter your amount :"))
    if value==-1:
        break
    
    category=str(input("Enter a category (food/travel/shopping/others):")).lower()
    
    if category=="food":
        food= food +  value
    elif category=="travel":
        travel= travel + value
    elif category=="shopping":
        shopping= shopping + value 
    elif category == "others":
        others = others + value           
   
        
        
total = food + travel + shopping + others           
        
        
print("\n========Expenses summary=======")
print("food:",food) 
print("travel:",travel)
print("shopping:",shopping)
print("others:",others)
print("total  :", total)       



