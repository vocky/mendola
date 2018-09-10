import pytest
from mendola import string
from nose.tools import assert_false, assert_true


def test_has_unique_chars():
    assert_false(string.has_unique_chars(None))
    assert_false(string.has_unique_chars(123))
    assert_true(string.has_unique_chars("abc"))
    assert_false(string.has_unique_chars("aaa"))
    assert_true(string.has_unique_chars(""))


if __name__ == '__main__':
    pytest.main([__file__])
