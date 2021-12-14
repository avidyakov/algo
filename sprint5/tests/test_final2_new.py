from dataclasses import dataclass

import pytest
from icecream import ic

from final2 import remove


@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


@pytest.fixture
def tree():
    return Node(
        10,
        left=Node(5, left=Node(1), right=Node(6)),
        right=Node(15, left=Node(11), right=Node(16))
    )


@pytest.fixture
def tree2():
    return Node(
        10,
        left=Node(5, right=Node(6)),
        right=Node(15, left=Node(11), right=Node(16))
    )


@pytest.fixture
def tree3():
    return Node(10, right=Node(20, left=Node(15)))


@pytest.fixture
def tree4():
    return Node(10, right=Node(15, right=Node(20)))


def test_remove(tree):
    actual = remove(tree, 20)
    expected = Node(
        10,
        left=Node(5, left=Node(1), right=Node(6)),
        right=Node(15, left=Node(11), right=Node(16))
    )
    assert actual == expected


def test_remove1(tree):
    actual = remove(tree, 16)
    expected = Node(
        10,
        left=Node(5, left=Node(1), right=Node(6)),
        right=Node(15, left=Node(11))
    )
    assert actual == expected


def test_remove2(tree):
    actual = remove(tree, 1)
    expected = Node(
        10,
        left=Node(5, right=Node(6)),
        right=Node(15, left=Node(11), right=Node(16))
    )
    assert actual == expected


def test_remove3(tree):
    actual = remove(tree, 5)
    expected = Node(
        10,
        left=Node(1, right=Node(6)),
        right=Node(15, left=Node(11), right=Node(16))
    )
    ic(actual)
    ic(actual.left.left)
    ic(expected)
    assert actual == expected


def test_remove4(tree2):
    actual = remove(tree2, 5)
    expected = Node(
        10,
        left=Node(6),
        right=Node(15, left=Node(11), right=Node(16))
    )
    assert actual == expected


def test_remove5(tree3):
    actual = remove(tree3, 10)
    expected = Node(15, right=Node(20))
    ic(actual, expected)
    assert actual == expected


def test_remove6(tree4):
    actual = remove(tree4, 15)
    expected = Node(10, right=Node(20))
    ic(actual, expected)
    assert actual == expected
