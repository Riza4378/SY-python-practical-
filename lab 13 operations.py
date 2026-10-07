Dictionary={"Name":"Riza", "Roll No": 94 , "Class": "S.Y" , "Div": "B" }
print(Dictionary)

#Accessing element
print(Dictionary["Name"])
print(Dictionary["Class"])

#Adding element in dictionary
Dictionary["Branch"]="AIML"
print(Dictionary)

#Updating Element
Dictionary["Roll No"]=108
print(Dictionary)

#Pop Operation
Dictionary.pop("Div")
print(Dictionary)

#Search Operation
if "Name" in Dictionary:
    print("Key Is Present.")
else:
    print("Key Is Not Present.") 

print(Dictionary.keys())       

print(Dictionary.values())

print(Dictionary.items())