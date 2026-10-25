try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")
