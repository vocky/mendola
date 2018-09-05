# -*- coding: UTF-8 -*-
from __future__ import print_function
import copy


def selection_sort(data, reverse=False):
    """
    Implement selection sort.
    :param data: list data
    :param reverse: if reverse is True, DESC, else ASC.
    :return: list data
    """
    iter(data)
    copy_data = copy.deepcopy(data)
    if len(copy_data) < 2:
        return copy_data

    def _swap(reverse_, data_, index_, min_index_):
        return data_[index_] < data_[min_index_] \
            if reverse_ else data_[index_] > data_[min_index_]

    for index in range(len(copy_data) - 1):
        min_index = index
        for last_index in range(index + 1, len(copy_data)):
            if reverse:
                min_index = last_index if copy_data[min_index] < copy_data[last_index] else min_index
            else:
                min_index = last_index if copy_data[min_index] > copy_data[last_index] else min_index
        if _swap(reverse, copy_data, index, min_index):
            copy_data[index], copy_data[min_index] = copy_data[min_index], copy_data[index]
    return copy_data


def insertion_sort(data, reverse=False):
    """
    Implement insertion sort.
    :param data: list data
    :param reverse: if reverse is True, DESC, else ASC.
    :return: list data
    """
    iter(data)
    copy_data = copy.deepcopy(data)
    if len(copy_data) < 2:
        return copy_data

    for i in range(1, len(copy_data)):
        for j in range(i):
            great_or_less = copy_data[i] > copy_data[j] if reverse else copy_data[i] < data[j]
            if great_or_less:
                temp = copy_data[i]
                copy_data[j + 1:i + 1] = copy_data[j:i]
                copy_data[j] = temp
    return copy_data


def quick_sort(data, reverse=False):
    """
    Implement quick sort.
    :param data: []
    :param reverse: if reverse is True, DESC, else ASC.
    :return: []
    """
    iter(data)
    copy_data = copy.deepcopy(data)
    if len(copy_data) < 2:
        return copy_data
    equal = []
    left = []
    right = []
    center_index = len(copy_data) // 2
    center_value = copy_data[center_index]
    for item in copy_data:
        great_or_less = item > center_value if reverse else item < center_value
        if item == center_value:
            equal.append(item)
        elif great_or_less:
            left.append(item)
        else:
            right.append(item)
    left_ = quick_sort(left, reverse)
    right_ = quick_sort(right, reverse)
    return left_ + equal + right_


def merge_sort(data, reverse=False):
    """
    Implement merge sort.
    :param data: []
    :param reverse: if reverse is True, DESC, else ASC.
    :return: []
    """
    iter(data)
    copy_data = copy.deepcopy(data)
    if len(copy_data) < 2:
        return copy_data

    def _merge(_left, _right, _reverse):
        s = 0
        r = 0
        result = []
        while s < len(_left) and r < len(_right):
            great_or_less = _left[s] > _right[r] if _reverse else _left[s] < _right[r]
            if great_or_less:
                result.append(_left[s])
                s += 1
            else:
                result.append(_right[r])
                r += 1
        # Copy remaining elements
        while s < len(_left):
            result.append(_left[s])
            s += 1
        while r < len(_right):
            result.append(_right[r])
            r += 1
        return result

    mid = len(copy_data) // 2
    left = copy_data[:mid]
    right = copy_data[mid:]
    left = merge_sort(left, reverse)
    right = merge_sort(right, reverse)
    return _merge(left, right, reverse)
