import pytest
from mendola import dp
from nose.tools import assert_equal


def fib(func):
    result = []
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(len(expected)):
        result.append(func(i))
    assert_equal(result, expected)


def test_fib():
    math = dp.Fibonacci()
    fib(math.fib_recursive)
    fib(math.fib_dynamic)
    fib(math.fib_iterative)


if __name__ == '__main__':
    pytest.main([__file__])
