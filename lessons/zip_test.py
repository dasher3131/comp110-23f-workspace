"""Test my zip function."""

__author__ = "730656282"

from zip import zip


def test_equal_length() -> None:
    """Test if it returns correctly when lists are equal."""
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    result = zip(keys, values)
    assert result == {'a': 1, 'b': 2, 'c': 3}


def test_unequal_length() -> None:
    """Test is it returns correctly when lists are not equal."""
    keys = ['a', 'b']
    values = [1, 2, 3]
    result = zip(keys, values)
    assert result == {}


def test_empty() -> None:
    """Tests if it returns an empty dictionary when lists are empty."""
    keys: list[str] = []
    values: list[int] = []
    result = zip(keys, values)
    assert result == {}