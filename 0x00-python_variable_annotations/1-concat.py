#!/usr/bin/env python3
"""
A module containing a function to concatenate two strings.

This module defines a type-annotated function `concat` that takes two
string arguments and returns their concatenation.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of the two strings.
    """
    return str1 + str2
