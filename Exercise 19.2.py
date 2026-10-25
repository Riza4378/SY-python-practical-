data = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}

try:
    key = input("Enter key name: ")
    print("Value:", data[key])

except KeyError:
    print("Item Not Found")
