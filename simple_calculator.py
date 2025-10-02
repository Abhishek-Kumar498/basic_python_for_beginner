import math

# Functions for operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def power(x, y): return x ** y
def modulus(x, y): return x % y
def square_root(x): return "Error! Negative number." if x < 0 else math.sqrt(x)

# Store history
history = []

while True:
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Modulus (%)")
    print("7. Square Root (√x)")
    print("8. Show History")
    print("9. Exit")

    choice = input("Enter choice (1-9): ")

    if choice == '9':
        print("Exiting Calculator... Goodbye! 👋")
        break

    # Handle square root (only 1 input needed)
    if choice == '7':
        try:
            num = float(input("Enter number: "))
            result = square_root(num)
            print(f"Result: {result}")
            history.append(f"√{num} = {result}")
        except ValueError:
            print("Invalid input! Enter numbers only.")
        continue

    # Handle other operations (2 inputs)
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            history.append(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = power(num1, num2)
            history.append(f"{num1}^{num2} = {result}")
        elif choice == '6':
            result = modulus(num1, num2)
            history.append(f"{num1} % {num2} = {result}")
        elif choice == '8':
            print("\n--- Calculation History ---")
            if history:
                for h in history:
                    print(h)
            else:
                print("No history available.")
            continue
        else:
            print("Invalid choice! Select from 1-9.")
            continue

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
