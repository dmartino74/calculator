from app.operation import operation

def calculate(op, *args):
    if op == "add":
        return operation.add(*args)
    elif op == "subtract":
        return operation.subtract(*args)
    elif op == "multiply":
        return operation.multiply(*args)
    elif op == "divide":
        return operation.divide(*args)
    elif op == "power":
        return operation.power(*args)
    elif op == "square":
        return operation.square(args[0])
    elif op == "sqrt":
        return operation.sqrt(args[0])
    elif op == "mod":
        return operation.mod(*args)
    elif op == "floor_divide":
        return operation.floor_divide(*args)
    else:
        raise ValueError(f"Unsupported operation: {op}")
    





if __name__ == "__main__":
    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, power, square, sqrt, mod, floor_divide")

    op = input("Enter operation: ").strip()

    if op in ["square", "sqrt"]:
        a = float(input("Enter one number: "))
        result = calculate(op, a)
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = calculate(op, a, b)

    print(f"Result: {result}")



