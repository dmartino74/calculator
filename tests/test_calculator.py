import pytest
from app.calculator.calculator import calculate, run_calculator
from unittest.mock import patch

# Dispatcher tests
def test_add():
    assert calculate("add", 2, 3) == 5

def test_subtract():
    assert calculate("subtract", 5, 2) == 3

def test_multiply():
    assert calculate("multiply", 4, 3) == 12

def test_divide():
    assert calculate("divide", 10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("divide", 5, 0)

def test_power():
    assert calculate("power", 2, 3) == 8

def test_square():
    assert calculate("square", 4) == 16

def test_sqrt():
    assert calculate("sqrt", 9) == 3

def test_sqrt_negative():
    with pytest.raises(ValueError):
        calculate("sqrt", -1)

def test_mod():
    assert calculate("mod", 10, 3) == 1

def test_floor_divide():
    assert calculate("floor_divide", 10, 3) == 3

def test_floor_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("floor_divide", 5, 0)

def test_unsupported_operation():
    with pytest.raises(ValueError) as excinfo:
        calculate("log", 10, 2)
    assert "Unsupported operation" in str(excinfo.value)

# REPL logic tests
def test_run_calculator_add(capsys):
    with patch("builtins.input", side_effect=["add", "2", "3"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Result: 5.0" in captured.out

def test_run_calculator_square(capsys):
    with patch("builtins.input", side_effect=["square", "4"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Result: 16.0" in captured.out

def test_run_calculator_invalid_op(capsys):
    with patch("builtins.input", side_effect=["log", "2", "3"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Unsupported operation" in captured.out

def test_run_calculator_divide_by_zero(capsys):
    with patch("builtins.input", side_effect=["divide", "5", "0"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out

def test_run_calculator_invalid_number(capsys):
    with patch("builtins.input", side_effect=["add", "two", "3"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out

def test_run_calculator_intro_message(capsys):
    with patch("builtins.input", side_effect=["add", "1", "1"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Welcome to the calculator!" in captured.out
        assert "Available operations" in captured.out

def test_run_calculator_unexpected_error(capsys):
    with patch("builtins.input", side_effect=["add", None, "3"]):
        run_calculator()
        captured = capsys.readouterr()
        assert "Unexpected error" in captured.out
