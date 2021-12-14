from test_c import node1, node2, node3, node4
from d import solution


def test_solution1(node1):
    assert solution(node1, 'node1') == 0


def test_solution2(node1):
    assert solution(node1, 'node3') == 2


def test_solution3(node1):
    assert solution(node1, 'node1005000') == -1
