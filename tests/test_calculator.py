import pytest
from app.calculator import add, subtract, multiply

def test_add_basic():
    result = add(2, 3)
    print(f"[TEST OUTPUT] add(2, 3) = {result}")
    assert result == 5

def test_add_zero():
    print("[TEST OUTPUT] add(0, 5) and add(5, 0)")
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_subtract_basic():
    result = subtract(10, 4)
    print(f"[TEST OUTPUT] subtract(10, 4) = {result}")
    assert result == 6

def test_subtract_negative_result_allowed():
    result = subtract(3, 5)
    print(f"[TEST OUTPUT] subtract(3, 5) = {result}")
    assert result == -2

def test_multiply_basic():
    result = multiply(4, 3)
    print(f"[TEST OUTPUT] multiply(4, 3) = {result}")
    assert result == 12

def test_types_must_be_ints():
    print("[TEST OUTPUT] Expecting TypeError for invalid input types")
    with pytest.raises(TypeError):
        add(2.5, 3)
    with pytest.raises(TypeError):
        subtract("5", 1)

def test_negative_input_raises_value_error():
    print("[TEST OUTPUT] Expecting ValueError for negative inputs")
    with pytest.raises(ValueError):
        add(-1, 2)
    with pytest.raises(ValueError):
        multiply(3, -4)

    print("ALL DONE!!")
