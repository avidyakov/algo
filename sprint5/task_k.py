import typing
from dataclasses import dataclass


@dataclass
class Node:
    right: typing.Optional['Node'] = None
    left: typing.Optional['Node'] = None
    value: int | None = None


def print_range(node: Node, left_border: int, right_border: int) -> None:
    """
    >>> node1 = Node(None, None, 2)
    >>> node2 = Node(None, node1, 1)
    >>> node3 = Node(None, None, 8)
    >>> node4 = Node(None, node3, 8)
    >>> node5 = Node(node4, None, 9)
    >>> node6 = Node(node5, None, 10)
    >>> node7 = Node(node2, node6, 5)
    >>> print_range(node7, 2, 8)
    2 5 8 8
    """
    if node.value < left_border:
        # Search right
        pass
    elif no:
        # Search left
        pass
