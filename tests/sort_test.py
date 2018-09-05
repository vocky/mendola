import pytest
from mendola import sort
from nose.tools import assert_raises, assert_equal


def test_selection_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    assert_equal(sort.selection_sort(a, True), b)
    assert_equal(a, a)
    assert_equal(sort.selection_sort(a), c)
    assert_equal(sort.selection_sort([]), [])
    assert_equal(sort.selection_sort([5]), [5])
    assert_raises(TypeError, sort.selection_sort, None)
    assert_raises(TypeError, sort.selection_sort, 12)


def test_insertion_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    assert_equal(sort.insertion_sort(a, True), b)
    assert_equal(a, a)
    assert_equal(sort.insertion_sort(a), c)
    assert_equal(sort.insertion_sort([]), [])
    assert_equal(sort.insertion_sort([5]), [5])
    assert_raises(TypeError, sort.insertion_sort, None)
    assert_raises(TypeError, sort.insertion_sort, 12)


def test_quick_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    assert_equal(sort.quick_sort(a, True), b)
    assert_equal(a, a)
    assert_equal(sort.quick_sort(a), c)
    assert_equal(sort.quick_sort([]), [])
    assert_equal(sort.quick_sort([5]), [5])
    assert_raises(TypeError, sort.quick_sort, None)
    assert_raises(TypeError, sort.quick_sort, 12)


def test_merge_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    assert_equal(sort.merge_sort(a, True), b)
    assert_equal(a, a)
    assert_equal(sort.merge_sort(a), c)
    assert_equal(sort.merge_sort([]), [])
    assert_equal(sort.merge_sort([5]), [5])
    assert_raises(TypeError, sort.merge_sort, None)
    assert_raises(TypeError, sort.merge_sort, 12)


if __name__ == '__main__':
    pytest.main([__file__])
