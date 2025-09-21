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





def xor(a, b):
    return a ^ b

def and_op(a, b):
    return a & b

def or_op(a, b):
    return a | b

def not_op(a):
    return ~a