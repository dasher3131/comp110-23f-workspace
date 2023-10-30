"""Summing the elements of a list using different loops."""

__author__ = "730656282"


def w_sum(vals: list[float]) -> float:
    """Calculates sum of numbers in this list usuing while loops."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        i: int = 0
        while i < len(vals):
            sum += vals[i]
            i += 1
        return sum


def f_sum(vals: list[float]) -> float:
    """Calculates sum of numbers in this list using a for in loop."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        for num in vals:
            sum += num
        return sum
    

def f_range_sum(vals: list[float]) -> float:
    """Calculates sum of numbers in this list using a for in range loop."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        i: int = 0
        for i in range(0, len(vals)):
            sum += vals[i]
        return sum