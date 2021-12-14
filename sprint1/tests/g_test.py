import pytest

from g import factorize_number


@pytest.mark.parametrize('test_input, expected', (
        (8, [2, 2, 2]),
        (100, [2, 2, 5, 5])
))
def test_factorize_number(test_input, expected):
    assert factorize_number(test_input) == expected
