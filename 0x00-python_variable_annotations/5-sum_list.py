#!/usr/bin/env python3
"""
A module containing a function to compute the sum of a list of floats.

This module defines a type-annotated function `sum_list` that takes a list
of floats as an argument and returns the sum of the elements as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return float(sum(input_list))
