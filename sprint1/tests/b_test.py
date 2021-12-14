import pytest

from b import are_all_of_the_same_parity


@pytest.mark.parametrize("test_input,expected", [
    ((1, 2, -3), False),
    ((7, 11, 7), True),
    ((6, -2, 0), True)
])
def test1(test_input, expected):
    assert are_all_of_the_same_parity(test_input) == expected
