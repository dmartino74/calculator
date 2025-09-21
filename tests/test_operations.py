from app.operation import operation

def test_add():
    assert operation.add(2, 3) == 5

def test_substract():
    assert operation.subtract(2, 1) == 1

def test_divide_by_zero():
    try:
        operation.divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
