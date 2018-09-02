import pytest
from mendola import string


def test_has_unique_chars():
    assert not string.has_unique_chars(None)
    assert not string.has_unique_chars(123)
    assert string.has_unique_chars("abc")
    assert not string.has_unique_chars("aaa")
    assert string.has_unique_chars("")


if __name__ == '__main__':
    pytest.main([__file__])