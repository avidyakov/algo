import sys
from dataclasses import dataclass


@dataclass
class Node:
    __slots__ = ('idx', 'adjacent')
    idx: int
    adjacent: list


def is_the_graff_complete(nodes):
    nodes_set = set(range(1, len(nodes) + 1))

    for node in nodes:
        actual_adjacent_set = {adj.idx for adj in node.adjacent} - {node.idx}
        expected_adjacent_set = nodes_set - {node.idx}

        if actual_adjacent_set != expected_adjacent_set:
            return False

    return True


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    nodes = [Node(idx, []) for idx in range(1, n + 1)]

    for _ in range(m):
        i, j = map(lambda a: int(a) - 1, sys.stdin.readline().split())
        node_i = nodes[i]
        node_j = nodes[j]
        node_i.adjacent.append(node_j)
        node_j.adjacent.append(node_i)

    result = 'YES' if is_the_graff_complete(nodes) else 'NO'
    print(result)


if __name__ == '__main__':
    main()
