import pytest
from mendola import sort


def test_selection_sort():
    a = [1, 6, 5]
    b = [6, 5, 1]
    c = [1, 5, 6]
    sort.selection_sort(a, True)
    assert a == b
    assert sort.selection_sort([]) == []
    sort.selection_sort(a)
    assert a == c


if __name__ == '__main__':
    pytest.main([__file__])