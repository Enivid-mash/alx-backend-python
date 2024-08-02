#!/usr/bin/env python3
"""
A module containing a function to compute the floor of a float.

This module defines a type-annotated function `floor` that takes a float
as an argument and returns its floor value as an integer.
"""


def floor(n: float) -> int:
    """
    Compute the floor of a float.

    Args:
        n (float): The floating-point number.

    Returns:
        int: The largest integer less than or equal to the input float.
    """
    return int(n)
