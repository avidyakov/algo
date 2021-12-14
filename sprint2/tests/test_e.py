import pytest

from e import solution


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


@pytest.fixture
def node4():
    return DoubleConnectedNode('node4')


@pytest.fixture
def node3():
    return DoubleConnectedNode('node3')


@pytest.fixture
def node2():
    return DoubleConnectedNode('node2')


@pytest.fixture
def node1():
    return DoubleConnectedNode('node1')


@pytest.fixture
def nodes(node1, node2, node3, node4):
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node2.prev = node1
    node3.prev = node2
    node4.prev = node3

    return node1


def get_all_nodes(node) -> list:
    result = [node.value]

    while node.next:
        node = node.next
        result.append(node.value)

    return result


def test_solution1(nodes):
    assert solution(nodes).value == 'node4'


def test_solution2(nodes):
    assert get_all_nodes(solution(nodes)) == ['node4', 'node3', 'node2', 'node1']
