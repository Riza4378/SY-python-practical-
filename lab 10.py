print("********Manage Product Prices********")

product_name=[]
product_price=[]

while True:
    print("1. Insert product")
    print("2. Display product")
    print("3. Update product")
    print("4. Delete product")
    print("5. serach product")
    print("6. sort product")
    print("7.Exit")
    
    choice =int(input("enter your choice:"))
    
    if choice==1:
      product=input("enter your product name :")
      product_name.append(product)
      
      price=int(input("enter your product price :"))
      product_price.append(price)
      
      print("product inserted successfully")
      
    elif choice==2:
        if len(product_name)==0:
            print("No products are available")
        else:
            print("product:-")
            
            for i in range(len(product_name)):
                print("product:",product_name[i], "price:",product_price[i])
                
    elif choice==3:
        product2 = input("Enter Product Name to Update :")
        
        if product2 in product_name:
            index = product_name.index(product2)
            new_price = int(input("Enter updated price :"))
            product_price[index] = new_price 
            print("Product updated successfully")
        else:
            print("Product not found")

    
        
                          
             
    elif choice==4:
        product3=input("enter product name to delete :")
        if product3 in product_name:
            index=product_name.index(product3)
            product_name.pop(index)
            product_price.pop(index)
            
            print("product delete successfully")
        else:
            print("product not found ")
            
    elif choice==5:
        product4=input("enter product name to search :")
        if product4 in product_name:
            index=product_name.index(product4)
            
            print("product:",product_name[index])
            print("price:",product_price[index])
            
            print("product found successfully")
        
        else:
            print("product not found")
            
    elif choice==6:
       for i in range(len(product_price)):
           for j in range(i + 1, len(product_price)):
               if product_price[i] > product_price[j]:
                   product_price[i], product_price[j] = product_price[j], product_price[i]
                   product_name[i], product_name[j] = product_name[j], product_name[i]
       print("Products sorted successfully")
                          
       print(product_name,product_price)

                   
                   
                       
    elif choice==7:
        print("-----thank you-----")
        break
    
    else:
        print("...invalid choice...")
    
        
        
                           
                       
       
       
                
            
            