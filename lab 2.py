print("***********grossary shop Billing calculator************")
rice_qty = float( input( "enter the quantity of rice (in kg):"))
rice_price_per_kg =50
rice_total = rice_qty * rice_price_per_kg

sugar_qty = float( input( "enter the quantity of sugar (in kg):"))
sugar_price_per_kg =40
sugar_total = sugar_qty * sugar_price_per_kg

Dal_qty = float( input( "enter the quantity of Dal  (in kg):"))
Dal_price_per_kg =80
Dal_total = Dal_qty * Dal_price_per_kg


print("************Bill details*************")
print("rice :", rice_total)
print("sugar :", sugar_total)
print("Dal:", Dal_total)

total_Bill = rice_total + sugar_total + Dal_total
print("total_Bill :",total_Bill)

discount = 0
if total_Bill >= 1000:
    discount = total_Bill*0.1
    print("discount:",discount)
elif total_Bill >=500:
    discount =total_Bill*0.05
    print("discount:" ,discount)
else:
    print("No discount")

final_Bill= total_Bill - discount
print("final_Bill :",final_Bill)        
       
