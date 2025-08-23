#!/usr/bin/env python3
"""
Simple calculator application for GitHub integration demo
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    """Main calculator function"""
    print("🧮 GitHub Calculator Demo")
    print("=" * 30)

    while True:
        try:
            print("\nChoose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Quit")

            choice = input("Enter choice (1-5): ")

            if choice == '5':
                print("Goodbye! 👋")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select 1-5.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            print(f"\n{num1} {operation} {num2} = {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
