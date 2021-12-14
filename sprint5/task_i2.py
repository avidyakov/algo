import typing
from dataclasses import dataclass
from itertools import permutations

from icecream import ic


@dataclass
class Node:
    value: int
    left: typing.Optional['Node'] = None
    right: typing.Optional['Node'] = None

    def get_depth(self) -> int:
        """
        >>> Node(2, Node(1), Node(3)).get_depth()
        1
        >>> Node(2, Node(1, Node(0), Node(1)), Node(3)).get_depth()
        2
        >>> Node(2, Node(1, Node(0, Node(-1)), Node(1)), Node(3)).get_depth()
        3
        """
        acc = 0

        if self.left or self.right:
            acc += 1

        if self.left:
            acc += self.left.get_depth()

        if self.right:
            acc += self.right.get_depth()

        return acc

    def get_array(self, array: list = None, idx: int = 1):
        """
        >>> Node(2, Node(1), Node(3)).get_array()
        [1, 2, 3]
        """
        if array is None:
            array = [-1] * 2 ** 3

        array[idx - 1] = self.value

        if self.left:
            self.left.get_array(array, idx * 2)

        if self.right:
            self.right.get_array(array, idx * 2 + 1)

        return array


def can_create_search_tree(values: tuple[int]) -> tuple[int]:
    head = cur_node = Node(values[0])

    for value in values[1:]:
        next_node = Node(value)

        if value > cur_node.value:
            cur_node.right = next_node
        else:
            cur_node.left = next_node

        cur_node = next_node

    return head


def get_search_trees(values: typing.Iterable[int]):
    acc = 0
    for perm in permutations(values):
        if can_create_search_tree(perm):
            acc += 1

    return acc


def main(number: int = None) -> None:
    """
    >>> main(2)
    2
    >>> main(3)
    5
    >>> main(4)
    14
    """
    number = number or int(input())
    print(get_search_trees(range(1, number + 1)))


if __name__ == '__main__':
    main()
