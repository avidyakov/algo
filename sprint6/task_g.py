import sys
from collections import deque
from dataclasses import dataclass

WHITE = 'w'
GRAY = 'g'
BLACK = 'b'


@dataclass
class Node:
    __slots__ = ('idx', 'color', 'adjacent', 'distance')
    idx: int
    color: str
    adjacent: list
    distance: int


def get_longest_path(vert: Node) -> int:
    planned = deque((vert,))
    vert.color = GRAY
    max_distance = 0

    while planned:
        vert = planned.popleft()
        vert.adjacent.sort(key=lambda node: node.idx)
        max_distance = max((max_distance, vert.distance))

        for adjacent in vert.adjacent:
            if adjacent.color == WHITE:
                adjacent.distance = vert.distance + 1
                adjacent.color = GRAY
                planned.append(adjacent)

        vert.color = BLACK

    return max_distance


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    nodes = [Node(idx, WHITE, [], 0) for idx in range(1, n + 1)]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        node_i = nodes[i - 1]
        node_j = nodes[j - 1]
        node_i.adjacent.append(node_j)
        node_j.adjacent.append(node_i)

    vertex = nodes[int(sys.stdin.readline()) - 1]
    print(get_longest_path(vertex))


if __name__ == '__main__':
    main()
