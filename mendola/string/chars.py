# -*- coding: UTF-8 -*-
from __future__ import print_function


def has_unique_chars(string):
    """
    Implement an algorithm to determine if a string has all unique characters.
    :param string: string
    :return: True/False
    """
    if string is None:
        return False
    if not isinstance(string, str):
        return False
    return len(set(string)) == len(string)

