"""Simple calculator with operations for two positive integers."""

def _validate_positive_int(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")

def add(a: int, b: int) -> int:
    """Return a + b for positive integers."""
    _validate_positive_int(a, b)
    return a + b

def subtract(a: int, b: int) -> int:
    """Return a - b for positive integers."""
    _validate_positive_int(a, b)
    return a - b

def multiply(a: int, b: int) -> int:
    """Return a * b for positive integers."""
    _validate_positive_int(a, b)
    return a * b
