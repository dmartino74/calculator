import pytest
from app.calculation import Calculation
from app.calculator import run_calculator
from unittest.mock import patch

# Dispatcher logic tests via Calculation class
def test_add():
    calc = Calculation("add", 2, 3)
    assert calc.result == 5

def test_subtract():
    calc = Calculation("subtract", 5, 2)
    assert calc.result == 3

def test_multiply():
    calc = Calculation("multiply", 4, 3)
    assert calc.result == 12

def test_divide():
    calc = Calculation("divide", 10, 2)
    assert calc.result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculation("divide", 5, 0)

def test_power():
    calc = Calculation("power", 2, 3)
    assert calc.result == 8

def test_square():
    calc = Calculation("square", 4)
    assert calc.result == 16

def test_sqrt():
    calc = Calculation("sqrt", 9)
    assert calc.result == 3

def test_sqrt_negative():
    with pytest.raises(ValueError):
        Calculation("sqrt", -1)

def test_mod():
    calc = Calculation("mod", 10, 3)
    assert calc.result == 1

def test_floor_divide():
    calc = Calculation("floor_divide", 10, 3)
    assert calc.result == 3

def test_floor_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculation("floor_divide", 5, 0)

def test_unsupported_operation():
    with pytest.raises(ValueError) as excinfo:
        Calculation("log", 10, 2)
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
