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



def test_xor():
    assert operation.xor(5, 3) == 6     # 0b0101 ^ 0b0011 = 0b0110

def test_and_op():
    assert operation.and_op(5, 3) == 1  # 0b0101 & 0b0011 = 0b0001

def test_or_op():
    assert operation.or_op(5, 3) == 7   # 0b0101 | 0b0011 = 0b0111

def test_not_op():
    assert operation.not_op(5) == -6    # ~5 = -6 in two's complement