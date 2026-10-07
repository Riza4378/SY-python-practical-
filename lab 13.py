Library={}

while True:
    print("1. Store Book Details")
    print("2. Update Book Details")
    print("3. Exit")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        Book_Id=int(input("Enter Book Id :"))
        Book_Name=input("Enter Book Name :")
        Book_Author=input("Enter Author Name :")
        Book_Price=float(input("Enter Book Price :"))
        
        Library[Book_Id]={"Name": Book_Name, "Author": Book_Author , "Price": Book_Price}
        print(Library)

        print("Book Details Add Successfully.")

    elif choice==2:
         Book_Id = int(input("Enter Book Id: "))

         if Book_Id in Library:
            Book_Name = input("Enter Book Name: ")
            Book_Author = input("Enter Author Name: ")
            Book_Price = float(input("Enter Book Price: "))

            Library[Book_Id]={"Name": Book_Name, "Author": Book_Author , "Price": Book_Price}
            print(Library)

    elif choice==3:
        print("Thank you! For Visiting Library.")
        break

    else:
        print("Invalid Choice.")