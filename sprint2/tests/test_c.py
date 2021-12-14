from dataclasses import dataclass
from typing import Optional, Any

import pytest

from c import solution


@dataclass
class Node:
    value: str
    next_item: Optional[Any]


def get_all_nodes(node) -> list:
    result = [node.value]

    while node.next_item:
        node = node.next_item
        result.append(node.value)

    return result


@pytest.fixture
def node4():
    return Node('node4', None)


@pytest.fixture
def node3(node4):
    return Node('node3', node4)


@pytest.fixture
def node2(node3):
    return Node('node2', node3)


@pytest.fixture
def node1(node2):
    return Node('node1', node2)


def test_solution(node1, node3, node4):
    new_head = solution(node1, 1)
    assert get_all_nodes(new_head) == [node1.value, node3.value, node4.value]

    new_head = solution(new_head, 2)
    assert get_all_nodes(new_head) == [node1.value, node3.value]


def test_solution1(node1, node2, node3, node4):
    new_head = solution(node1, 0)
    assert get_all_nodes(new_head) == [node2.value, node3.value, node4.value]
