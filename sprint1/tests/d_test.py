import pytest

from d import get_randomness


@pytest.mark.parametrize('input,expected', (
        ((-1, -10, -8, 0, 2, 0, 5), 3),
        ((1, 2, 5, 4, 8), 2)
))
def test1(input, expected):
    assert get_randomness(input) == expected
