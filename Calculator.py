import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            choice = int(choice)
            if choice == 5:
                num3 = float(input("Enter the number: "))
                print("Square root of", num3, "=", math.sqrt(num3))
                continue
            if choice == 6:
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 4:
                print(num1, "/", num2, "=", divide(num1, num2))

        else:
            print("Invalid input")

calculator()
