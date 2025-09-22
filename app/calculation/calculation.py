# app/calculation.py

from app.operation import (
    add, subtract, multiply, divide,
    power, square, sqrt, mod, floor_divide
)

class Calculation:
    def __init__(self, operation, *args):
        self.operation = operation
        self.args = args
        self.result = self._perform()

    def _perform(self):
        if self.operation == "add":
            return add(*self.args)
        elif self.operation == "subtract":
            return subtract(*self.args)
        elif self.operation == "multiply":
            return multiply(*self.args)
        elif self.operation == "divide":
            return divide(*self.args)
        elif self.operation == "power":
            return power(*self.args)
        elif self.operation == "square":
            return square(self.args[0])
        elif self.operation == "sqrt":
            return sqrt(self.args[0])
        elif self.operation == "mod":
            return mod(*self.args)
        elif self.operation == "floor_divide":
            return floor_divide(*self.args)
        else:
            raise ValueError(f"Unsupported operation: {self.operation}")
