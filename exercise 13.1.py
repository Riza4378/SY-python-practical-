Inventory = {}

while True:
    print("1. Store Item Details")
    print("2. Sell Item")
    print("3. Display Inventory")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))
    
    print("------------------------------------")
    if choice == 1:
        Item_Name = input("Enter Item Name: ")
        Stock = int(input("Enter Stock Quantity: "))

        Inventory[Item_Name] = Stock
        print(Inventory)
        print("Item Added Successfully.")
        print("------------------------------------")
        
    elif choice == 2:
        Item_Name = input("Enter Item Name: ")

        if Item_Name in Inventory:
            Quantity = int(input("Enter Quantity Sold: "))

            if Quantity <= Inventory[Item_Name]:
                Inventory[Item_Name] = Inventory[Item_Name] - Quantity

                print(Inventory)
                print("Sale Completed Successfully.")

                if Inventory[Item_Name] == 0:
                    print("WARNING: Stock is ZERO!")

            else:
                print("Not Enough Stock Available.")

        else:
            print("Item Not Found.")

    elif choice == 3:
        print("Current Inventory:")
        print(Inventory)
        print("------------------------------------")

    elif choice == 4:
        print("Thank You! For Visiting Inventory Manager.")
        print("------------------------------------")
        break

    else:
        print("Invalid Choice.")
