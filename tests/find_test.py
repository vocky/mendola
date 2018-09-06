import pytest
from mendola import find
from nose.tools import assert_raises, assert_equal


def test_find_not_in_array():
    max_size = 32
    assert_raises(TypeError, find.find_not_in_array, None, max_size)
    assert_raises(TypeError, find.find_not_in_array, [], max_size)
    assert_raises(TypeError, find.find_not_in_array, [1, 'a'], max_size)
    data = [item for item in range(30)]
    data.append(31)
    assert_equal(find.find_not_in_array(data, max_size), 30)
    data = [item for item in range(32)]
    assert_equal(find.find_not_in_array(data, max_size), None)


if __name__ == '__main__':
    pytest.main([__file__])