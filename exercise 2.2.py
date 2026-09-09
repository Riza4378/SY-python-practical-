print("===== BILLING SUMMARY =====")

amount = float(input("Enter total purchase amount: "))
discount = float(input("Enter discount percentage: "))

discount_amount = amount * discount / 100
final_amount = amount - discount_amount
print("\n===== BILLING SUMMARY =====")

print("Purchase Amount :", amount)
print("Discount (%) :", discount)
print("Discount Amount :", discount_amount)

print("----------------------------")
print("Final Payable :", final_amount)