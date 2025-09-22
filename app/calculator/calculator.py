# app/calculator.py

from app.calculation import Calculation

def run_calculator():
    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, power, square, sqrt, mod, floor_divide")

    op = input("Enter operation: ").strip()

    try:
        if op in ["square", "sqrt"]:
            a = float(input("Enter one number: "))
            calc = Calculation(op, a)
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calc = Calculation(op, a, b)

        print(f"Result: {calc.result}")
    except ValueError as ve:
        if "Unsupported operation" in str(ve):
            print(str(ve))  # e.g. "Unsupported operation: log"
        else:
            print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":  # pragma: no cover
    run_calculator()
