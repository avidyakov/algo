from dataclasses import dataclass

import pytest

from final1 import broken_search, binary_search


@dataclass
class BrokenSearchCase:
    input_list: list
    input_search: int
    expected: int


BROKEN_SEARCH_CASES = (
    BrokenSearchCase(input_list=[19, 21, 100, 101, 1, 4, 5, 7, 12], input_search=5, expected=6),
    BrokenSearchCase(input_list=[5, 1], input_search=1, expected=1),
    BrokenSearchCase(input_list=[3, 6, 7], input_search=8, expected=-1),
    BrokenSearchCase(input_list=[19, 21, 100, 101, 1, 4, 5], input_search=5, expected=6),
    BrokenSearchCase(input_list=[19, 21, 1, 4, 5], input_search=19, expected=0),
    BrokenSearchCase(input_list=[19, 1, 4, 5], input_search=1, expected=1),
    BrokenSearchCase(input_list=[5, 10, 2], input_search=2, expected=2),
)


@pytest.mark.parametrize('case', BROKEN_SEARCH_CASES)
def test_broken_search(case):
    assert broken_search(case.input_list, case.input_search) == case.expected


@dataclass
class BinarySearchCase:
    input_list: list
    input_search: int
    expected: int


BINARY_SEARCH_CASES = (
    BinarySearchCase([1, 2, 3, 4], input_search=4, expected=3),
    BinarySearchCase(input_list=[1, 2, 3, 4], input_search=2, expected=1),
    BinarySearchCase(input_list=[3, 6, 7], input_search=8, expected=-1),
    BinarySearchCase(input_list=[1, 2, 3, 4], input_search=1, expected=0)
)


@pytest.mark.parametrize('case', BINARY_SEARCH_CASES)
def test_binary_search(case):
    assert binary_search(case.input_list, case.input_search, 0, len(case.input_list)) == case.expected
