import pytest

from h import binary_sum


@pytest.mark.parametrize('test_input,expected', (
        (('1010', '1011'), '10101'),
        (('1', '1'), '10'),
        (('10', '0'), '10'),
        (('11001', '10111100'), '11010101')
))
def test_binary_sum(test_input, expected):
    assert binary_sum(*test_input) == expected
