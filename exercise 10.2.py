products = ["laptop","Mobile","Mouse","printer","scanner"]

item=input("enter product name to search:")

if item in products:
    index=products.index(item)
    print("item found!")
    print("product:",item)
    print("index location:",index)
else:
    print("item not found in inventory.")      