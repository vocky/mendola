import pytest
from mendola import queues
from nose.tools import assert_equal


def test_priority_queue():
    priority_queue = queues.PriorityQueue()
    assert_equal(priority_queue.extract_min(), None)
    priority_queue.insert(queues.PriorityQueueNode('a', 20))
    priority_queue.insert(queues.PriorityQueueNode('b', 5))
    priority_queue.insert(queues.PriorityQueueNode('c', 15))
    priority_queue.insert(queues.PriorityQueueNode('d', 22))
    priority_queue.insert(queues.PriorityQueueNode('e', 40))
    priority_queue.insert(queues.PriorityQueueNode('f', 3))
    priority_queue.decrease_key('f', 2)
    priority_queue.decrease_key('a', 19)
    min_list = []
    while priority_queue.array:
        min_list.append(priority_queue.extract_min().key)
    assert_equal(min_list, [2, 5, 15, 19, 22, 40])


def test_stack():
    stack = queues.Stack()
    assert_equal(stack.peek(), None)
    assert_equal(stack.pop(), None)

    stack.push(5)
    assert_equal(stack.pop(), 5)
    assert_equal(stack.peek(), None)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert_equal(stack.pop(), 3)
    assert_equal(stack.peek(), 2)
    assert_equal(stack.pop(), 2)
    assert_equal(stack.peek(), 1)
    assert_equal(stack.is_empty(), False)
    assert_equal(stack.pop(), 1)
    assert_equal(stack.peek(), None)
    assert_equal(stack.is_empty(), True)


if __name__ == '__main__':
    pytest.main([__file__])
