import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, breadth):
    return length * breadth

while True:
    print("\nGeometric Area Calculator")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        r = float(input("Enter radius of circle: "))
        print("Area of Circle =", area_circle(r))

    elif choice == '2':
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))
        print("Area of Rectangle =", area_rectangle(l, b))

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")