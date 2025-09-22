from app.operation import operation

def test_add():
    assert operation.add(2, 3) == 5

def test_substract():
    assert operation.subtract(2, 1) == 1

def test_multiply():
    assert operation.multiply(2, 2) == 4

def test_divide_by_zero():
    try:
        operation.divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False









def test_power():
    assert operation.power(2, 3) == 8
    assert operation.power(5, 0) == 1

def test_square():
    assert operation.square(4) == 16
    assert operation.square(-3) == 9

def test_sqrt():
    assert operation.sqrt(9) == 3
    assert operation.sqrt(0) == 0
    assert round(operation.sqrt(2), 5) == round(2 ** 0.5, 5)

def test_sqrt_negative():
    try:
        operation.sqrt(-1)
    except ValueError:
        assert True
    else:
        assert False

def test_mod():
    assert operation.mod(10, 3) == 1
    assert operation.mod(7, 7) == 0

def test_floor_divide():
    assert operation.floor_divide(10, 3) == 3
    assert operation.floor_divide(9, 2) == 4

def test_floor_divide_by_zero():
    try:
        operation.floor_divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False


