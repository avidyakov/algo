import pytest

from node import Node
from task_j import insert


@pytest.fixture
def root_node():
    return Node(7, right=Node(8, left=Node(7)))


def test_insert(root_node):
    result = insert(root_node, 7)
    assert result is not None
    assert root_node.right.left.right.value == 7


def test_insert2(root_node):
    result = insert(root_node, 6)
    assert result is not None
    assert root_node.value == 7
    assert root_node.left.value == 6
    assert root_node.right.value == 8
    assert root_node.right.left.value == 7
