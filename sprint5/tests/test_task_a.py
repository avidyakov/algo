import typing
from dataclasses import dataclass

import pytest

from task_a import solution


@dataclass
class Node:
    value: int
    left: typing.Optional['Node'] = None
    right: typing.Optional['Node'] = None


@pytest.fixture
def tree1():
    return Node(
        value=10
    )


@pytest.fixture
def tree2():
    return Node(
        value=10,
        left=Node(
            value=20,
            left=Node(
                value=33
            ),
            right=Node(
                value=32
            ),
        ),
        right=Node(
            value=21,
            left=Node(
                value=31
            ),
            right=Node(
                value=30
            ),
        )
    )


@pytest.fixture
def tree3():
    return Node(
        value=10,
        left=Node(
            value=20,
            left=Node(
                value=33
            ),
            right=Node(
                value=32,
                right=Node(
                    value=20,
                    left=Node(
                        value=33,
                        right=Node(
                            value=20,
                            left=Node(
                                value=33
                            ),
                            right=Node(
                                value=32,
                                right=Node(
                                    value=20,
                                    left=Node(
                                        value=1_000_000
                                    ),
                                ),
                            ),
                        )
                    ),
                    right=Node(
                        value=32
                    ),
                ),
            ),
        ),
        right=Node(
            value=21,
            left=Node(
                value=31
            ),
            right=Node(
                value=30
            ),
        )
    )


def test_solution(tree1):
    assert solution(tree1) == 10


def test_solution2(tree2):
    assert solution(tree2) == 33


def test_solution3(tree3):
    assert solution(tree3) == 1_000_000
