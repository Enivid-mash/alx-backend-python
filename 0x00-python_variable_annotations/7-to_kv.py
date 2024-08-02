#!/usr/bin/env python3
"""
A module containing a function to create a tuple with a string and
the square of a number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number, which can be either an int or a float

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
                    and the second element is the square of `v` as a float.
    """
    return (k, float(v * v))
