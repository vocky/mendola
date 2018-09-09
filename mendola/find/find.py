# -*- coding: UTF-8 -*-
from __future__ import print_function
from bitstring import BitArray


def find_not_in_array(array_data, max_size):
    """
    find an int not in the input
    :param array_data: []
    :param max_size: great than len(array_data)
    :return: None or index
    """
    if not array_data:
        raise TypeError('array cannot be None or empty')
    bit_vector = BitArray(max_size)
    for item in array_data:
        if not isinstance(item, int):
            raise TypeError('item must be int')
        bit_vector[item] = True
    for index, item in enumerate(bit_vector):
        if not item:
            return index
    return None
