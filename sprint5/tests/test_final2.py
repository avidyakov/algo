from dataclasses import dataclass

import pytest

from final2_old import remove


@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


@pytest.fixture
def tree():
    return Node(2, left=Node(1), right=Node(3))


@pytest.fixture
def tree2():
    return Node(
        10,
        left=Node(
            5,
            left=Node(3),
            right=Node(7)
        ),
        right=Node(
            15,
            left=Node(11),
            right=Node(17)
        )
    )


@pytest.fixture
def tree3():
    return Node(
        50,
        left=Node(25),
        right=Node(
            75,
            right=Node(
                100,
                left=Node(90),
                right=Node(110)
            )
        )
    )


@pytest.fixture
def tree4():
    return Node(
        5,
        left=Node(1, right=Node(3, left=Node(2))),
        right=Node(10, left=Node(8, left=Node(6)))
    )


@pytest.fixture
def tree5():
    return Node(
        460,
        left=Node(355, left=Node(270)),
        right=Node(
            818,
            left=Node(
                649,
                left=Node(626, left=Node(568, right=Node(609))),
                right=Node(708)
            ),
            right=Node(840)
        )
    )


def test_remove(tree):
    removed = remove(tree, 1)
    assert removed.value == 2
    assert removed.left is None
    assert removed.right.value == 3


def test_remove2(tree2):
    removed = remove(tree2, 5)
    assert removed.value == 10
    assert removed.right.value == 15
    assert removed.left.value == 3
    assert removed.left.right.value == 7
    assert removed.left.left is None


def test_remove3(tree2):
    removed = remove(tree2, 11)
    assert removed.value == 10
    assert removed.right.left is None


def test_remove4(tree2):
    removed = remove(tree2, 10)
    assert removed.value == 7
    assert removed.right.value == 15
    assert removed.left.value == 5
    assert removed.left.left.value == 3
    assert removed.left.right is None


def test_remove5(tree):
    removed = remove(tree, 2)
    assert removed.value == 1
    assert removed.left is None
    assert removed.right.value == 3


def test_remove6(tree):
    removed = remove(tree, 100)
    assert removed.value == 2
    assert removed.left.value == 1
    assert removed.right.value == 3


def test_remove7(tree3):
    removed = remove(tree3, 100)
    assert removed.value == 50
    assert removed.left.value == 25
    assert removed.right.value == 75
    assert removed.right.left is None
    assert removed.right.right.value == 90
    assert removed.right.right.left is None
    assert removed.right.right.right.value == 110


def test_remove8(tree4):
    removed = remove(tree4, 10)
    assert removed.value == 5
    assert removed.left.value == 1
    assert removed.right.value == 8
    assert removed.right.right is None
    assert removed.right.left.value == 6
