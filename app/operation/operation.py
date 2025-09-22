# app/operation/operation.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b





def power(a, b):
    return a ** b

def square(a):
    return a ** 2

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5

def mod(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a // b