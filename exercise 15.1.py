def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit:", result)

    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(f)
        print("Temperature in Celsius:", result)

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")