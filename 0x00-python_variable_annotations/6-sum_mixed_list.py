#!/usr/bin/env python3
"""
A module containing a function to compute the sum of a list of integers
and floats.

This module defines a type-annotated function `sum_mixed_list` that takes a
list
containing both integers and floats as an argument and returns the sum of
the elements as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): Alist containing integers andfloats

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return float(sum(mxd_lst))
