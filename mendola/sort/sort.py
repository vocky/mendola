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


def insertion_sort(data, reverse=False):
    """
    Implement insertion sort.
    :param data: list data
    :param reverse: if reverse is True, DESC, else ASC.
    :return: list data
    """
    iter(data)
    if len(data) < 2:
        return data

    for i in range(1, len(data)):
        for j in range(i):
            great_or_less = data[i] > data[j] if reverse else data[i] < data[j]
            if great_or_less:
                temp = data[i]
                data[j + 1:i + 1] = data[j:i]
                data[j] = temp
    return data
