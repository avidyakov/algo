import typing
from dataclasses import dataclass

import pytest

from task_b import solution


@dataclass
class Node:
    value: int
    left: typing.Optional['Node'] = None
    right: typing.Optional['Node'] = None


@pytest.fixture
def search_tree():
    return Node(
        value=10,
        left=Node(
            value=5,
            left=Node(
                value=1
            ),
            right=Node(
                value=6
            )
        ),
        right=Node(
            value=15
        )
    )


@pytest.fixture
def not_search_tree():
    return Node(
        value=10,
        left=Node(
            value=5,
            left=Node(
                value=1
            ),
            right=Node(
                value=1
            )
        ),
        right=Node(
            value=15
        )
    )


def test_solution1(search_tree):
    assert solution(search_tree) is True


def test_solution2(not_search_tree):
    assert solution(not_search_tree) is False
