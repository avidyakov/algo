import sys
from dataclasses import dataclass
from collections import deque

WHITE = 'w'
GRAY = 'g'
BLACK = 'b'


@dataclass
class Node:
    __slots__ = ('idx', 'color', 'adjacent')
    idx: int
    color: str
    adjacent: list


def dfs(vert: Node):
    planned = deque((vert, ))
    vert.color = GRAY
    visited = []

    while planned:
        vert = planned.popleft()
        visited.append(vert.idx)
        vert.adjacent.sort(key=lambda node: node.idx)

        for adjacent in vert.adjacent:
            if adjacent.color == WHITE:
                adjacent.color = GRAY
                planned.append(adjacent)

        vert.color = BLACK

    return visited


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    nodes = [Node(idx, WHITE, []) for idx in range(1, n + 1)]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        node_i = nodes[i - 1]
        node_j = nodes[j - 1]
        node_i.adjacent.append(node_j)
        node_j.adjacent.append(node_i)

    vertex = nodes[int(sys.stdin.readline()) - 1]
    print(*dfs(vertex))


if __name__ == '__main__':
    main()
