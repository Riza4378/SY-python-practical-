dictionary={"Name":"Riza" , "Roll No":94 , "Div":"B" , "Class":"SY" , "Marks":8.69}

print(dictionary)

#Accessing Element
print(dictionary["Name"])
print(dictionary["Roll No"])
print(dictionary["Div"])
print(dictionary["Class"])
print(dictionary["Marks"])

#insertion
dictionary["Address"]="vita"
print(dictionary)

#deletion
dictionary.pop("Marks")
print(dictionary)

#searching
if "Name" in dictionary:
    print("Key is present")

else:
    print("Key is absent")

#Accessing only keys
print(dictionary.keys())

#Accessing only elements
print(dictionary.values())

#Accessing boths
print(dictionary.items())




