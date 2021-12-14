import typing
from itertools import permutations, repeat


def get_tree(values: tuple[int]) -> list[int]:
    """
    >>> get_tree((1, 2, 3))
    [1, None, 2, None, None, None, 3]
    >>> get_tree((1, 3, 2))
    [1, None, 3, None, None, 2]
    """
    tree = [values[0]]
    parent_idx = 1

    for idx, next_node in enumerate(values[1:], 2):
        parent = tree[parent_idx - 1]
        parent_idx *= 2

        if next_node > parent:
            parent_idx += 1

        if len(tree) <= parent_idx - 1:
            tree.extend(repeat(None, parent_idx - len(tree)))

        tree[parent_idx - 1] = next_node

    return tree


def get_trees(values: typing.Iterable[int]) -> set:
    trees = set()

    for perm in permutations(values):
        tree = get_tree(perm)
        trees.add(tuple(tree))

    return trees


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
    print(len(get_trees(range(1, number + 1))))


if __name__ == '__main__':
    main()
