"""Combining two lists into a dictionary."""

__author__ = "730656282"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Function to combine two lists into one dictionary."""
    if len(keys) != len(values) or not keys or not values:
        return {}
    return {keys[i]: values[i] for i in range(len(keys))}