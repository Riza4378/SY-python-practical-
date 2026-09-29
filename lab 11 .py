Bus=[ ["a","a","a"],
      ["a","a","a"],
      ["a","a","a"]]

print("\n-------------------------------")
print("       BUS SEAT RESERVATION")
print("---------------------------------")

for i in range(3):
    print( Bus[i])

print("\n**** please select your seat ****") 
   
row = int(input("Enter your row number:"))
seat = int(input("Enter your seat number :"))

print("--------------------------------")

if Bus[row-1][seat-1] =="a":
    Bus[row-1][seat-1]="r"
    print("your seat is reserved..!")
else:
    print("seat is already reserved..!")
    
print("--------------------------------")   
 
for i in range(3):
    print(Bus[i])
    
print("==============================")    
    
    
    
    


    
    


