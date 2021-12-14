from dataclasses import dataclass

import pytest

from k import merge, merge_sort


@dataclass
class MergeCase:
    input_array: list
    input_left: int
    input_middle: int
    input_right: int
    expected_return: list


MERGE_CASES = (
    pytest.param(MergeCase(
        input_array=[1, 4, 9, 2, 10, 11],
        input_left=0,
        input_middle=3,
        input_right=6,
        expected_return=[1, 2, 4, 9, 10, 11]
    ), id='source_test'),
)


@pytest.mark.parametrize('test_case', MERGE_CASES)
def test_merge(test_case):
    actual_result = merge(test_case.input_array, test_case.input_left, test_case.input_middle, test_case.input_right)
    assert actual_result == test_case.expected_return


@dataclass
class MergeSortCase:
    input_array: list
    input_left: int
    input_right: int
    expected_array: list


MERGE_SORT_CASES = (
    pytest.param(MergeSortCase(
        input_array=[1, 4, 2, 10, 1, 2],
        input_left=0,
        input_right=6,
        expected_array=[1, 1, 2, 2, 4, 10]
    ), id='source_test'),
)


@pytest.mark.parametrize('test_case', MERGE_SORT_CASES)
def test_merge_sort(test_case):
    merge_sort(test_case.input_array, test_case.input_left, test_case.input_right)
    assert test_case.input_array == test_case.expected_array
