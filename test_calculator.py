# tests/test_calculator.py
def test_add():
    from calculator import calculator
    assert calculator.add(2, 3) == 5
