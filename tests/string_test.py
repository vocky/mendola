import pytest
from mendola import string
from nose.tools import assert_equal


def test_has_unique_chars():
    assert not string.has_unique_chars(None)
    assert not string.has_unique_chars(123)
    assert string.has_unique_chars("abc")
    assert not string.has_unique_chars("aaa")
    assert string.has_unique_chars("")


def test_priority_queue():
    priority_queue = string.PriorityQueue()
    assert_equal(priority_queue.extract_min(), None)
    priority_queue.insert(string.PriorityQueueNode('a', 20))
    priority_queue.insert(string.PriorityQueueNode('b', 5))
    priority_queue.insert(string.PriorityQueueNode('c', 15))
    priority_queue.insert(string.PriorityQueueNode('d', 22))
    priority_queue.insert(string.PriorityQueueNode('e', 40))
    priority_queue.insert(string.PriorityQueueNode('f', 3))
    priority_queue.decrease_key('f', 2)
    priority_queue.decrease_key('a', 19)
    min_list = []
    while priority_queue.array:
        min_list.append(priority_queue.extract_min().key)
    assert_equal(min_list, [2, 5, 15, 19, 22, 40])


if __name__ == '__main__':
    pytest.main([__file__])