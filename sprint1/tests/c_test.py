import sys

import pytest

from c import get_coordinates_of_neighbors, main


@pytest.mark.parametrize('input1,input2,expected', (
        (
                (3, 0), (4, 3), [[2, 0], [3, 1]]
        ),
        (
                (0, 0), (4, 3), [[1, 0], [0, 1]]
        )
))
def test1(input1, input2, expected):
    assert get_coordinates_of_neighbors(input1, input2) == expected



