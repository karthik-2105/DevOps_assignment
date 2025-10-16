import pytest
from app.calculator import add, subtract, multiply

def test_add_basic():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_subtract_basic():
    assert subtract(10, 4) == 6

def test_subtract_negative_result_allowed():
    # subtraction can produce negative results (but inputs must be positive)
    assert subtract(3, 5) == -2

def test_multiply_basic():
    assert multiply(4, 3) == 12

def test_types_must_be_ints():
    with pytest.raises(TypeError):
        add(2.5, 3)
    with pytest.raises(TypeError):
        subtract("5", 1)

def test_negative_input_raises_value_error():
    with pytest.raises(ValueError):
        add(-1, 2)
    with pytest.raises(ValueError):
        multiply(3, -4)
