from app.operation import (
    add, subtract, multiply, divide,
    power, square, sqrt, mod, floor_divide
)

def calculate(op, *args):
    if op == "add":
        return add(*args)
    elif op == "subtract":
        return subtract(*args)
    elif op == "multiply":
        return multiply(*args)
    elif op == "divide":
        return divide(*args)
    elif op == "power":
        return power(*args)
    elif op == "square":
        return square(args[0])
    elif op == "sqrt":
        return sqrt(args[0])
    elif op == "mod":
        return mod(*args)
    elif op == "floor_divide":
        return floor_divide(*args)
    else:
        raise ValueError(f"Unsupported operation: {op}")

def run_calculator():
    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, power, square, sqrt, mod, floor_divide")

    op = input("Enter operation: ").strip()

    try:
        if op in ["square", "sqrt"]:
            a = float(input("Enter one number: "))
            result = calculate(op, a)
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(op, a, b)

        print(f"Result: {result}")
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

def test_run_calculator_unexpected_error(capsys):
    # Simulate a crash by passing a string that causes float() to fail
    with patch("builtins.input", side_effect=["add", "two", "three"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out
