print("===== GROCERY BILL =====")

name1 = input("\n Enter item 1: ")
qty1 = int(input("Enter quantity: "))
price1 = float(input("Enter price: "))

name2 = input("\n Enter item 2: ")
qty2 = int(input("Enter quantity: "))
price2 = float(input("Enter price: "))

name3 = input("\n Enter item 3: ")
qty3 = int(input("Enter quantity: "))
price3 = float(input("Enter price: "))

amount1 = qty1 * price1
amount2 = qty2 * price2
amount3 = qty3 * price3
total = amount1 + amount2 + amount3

print("\n===== FINAL BILL =====")

print("Name \t qty \t Ammount")
print("-----------------------")
print(name1, "\t", qty1, "\t", amount1)
print(name2, "\t", qty2, "\t", amount2)
print(name3, "\t", qty3, "\t", amount3)
print("----------------------")
print("Total Bill =", total) 