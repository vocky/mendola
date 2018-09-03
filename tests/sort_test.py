import pytest
from mendola import sort
from nose.tools import assert_raises, assert_equal


def test_selection_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    sort.selection_sort(a, True)
    assert_equal(a, b)
    sort.selection_sort(a)
    assert_equal(a, c)
    assert_equal(sort.selection_sort([]), [])
    assert_raises(TypeError, sort.selection_sort, None)
    assert_raises(TypeError, sort.selection_sort, 12)


def test_insertion_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    sort.insertion_sort(a, True)
    assert_equal(a, b)
    sort.insertion_sort(a)
    assert_equal(a, c)
    assert_equal(sort.insertion_sort([]), [])
    assert_raises(TypeError, sort.insertion_sort, None)
    assert_raises(TypeError, sort.insertion_sort, 12)


if __name__ == '__main__':
    pytest.main([__file__])
