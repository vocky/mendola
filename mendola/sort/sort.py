# -*- coding: UTF-8 -*-
from __future__ import print_function


def selection_sort(data, reverse=False):
    """
    Implement selection sort.
    :param data: list data
    :param reverse: if reverse is True, DESC, else ASC.
    :return: list data
    """
    iter(data)
    if len(data) < 2:
        return data

    def _swap(reverse_, data_, index_, min_index_):
        return data_[index_] < data_[min_index_] \
            if reverse_ else data_[index_] > data_[min_index_]

    for index in range(len(data) - 1):
        min_index = index
        for last_index in range(index + 1, len(data)):
            if reverse:
                min_index = last_index if data[min_index] < data[last_index] else min_index
            else:
                min_index = last_index if data[min_index] > data[last_index] else min_index
        if _swap(reverse, data, index, min_index):
            data[index], data[min_index] = data[min_index], data[index]
    return data
