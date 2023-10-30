"""EX04 - lists!"""

__author__: str = "730656282"


def all(number_list: list[int], number: int) -> bool:
    """See if numbers in list are equal to input."""
    i: int = 0
    if len(number_list) == 0:
        return False
    while i < len(number_list):
        if number_list[i] != number:
            return False
        i += 1
    return True


def max(number_list: list[int]) -> int:
    """Find the maximum number in list."""
    if len(number_list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    max: int = number_list[0]
    while i < len(number_list):
        if number_list[i] > max:
            max = number_list[i]
        i += 1
    return max


def is_equal(num1: list[int], num2: list[int]) -> bool:
    """Checks if lists are equal."""
    i: int = 0
    check: bool = True
    if len(num1) != len(num2):
        return False
    while i < len(num1):
        if num1[i] != num2[i]:
            check = False
        i += 1
    return check