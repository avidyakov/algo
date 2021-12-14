import pytest

from node import Node
from task_b2 import solution, get_level


@pytest.fixture
def tree():
    return Node(1, Node(2), Node(0))


@pytest.fixture
def tree2(tree):
    tree.right.left = Node(3)
    tree.right.right = Node(6)
    return tree


@pytest.fixture
def tree3(tree2):
    tree2.right.left.left = Node(100)
    return tree2


def test_get_level(tree):
    assert get_level(tree) == 2


def test_get_level2(tree2):
    assert get_level(tree2) == 3


def test_get_level3(tree3):
    assert get_level(tree3) == 4


def test_solution(tree):
    assert solution(tree) is True


def test_solution2(tree2):
    assert solution(tree2) is True


def test_solution3(tree3):
    assert solution(tree3) is False
