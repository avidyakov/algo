import sys
from dataclasses import dataclass
from collections import deque

WHITE_COLOR = 'w'
GRAY_COLOR = 'g'
BLACK_COLOR = 'b'


@dataclass
class Node:
    __slots__ = ('idx', 'dist', 'color', 'adjacent')
    idx: int
    dist: int
    color: str
    adjacent: list


def dfs(vert: Node) -> None:
    vert.color = GRAY_COLOR
    vert.dist = 0
    planned = deque((vert, ))

    while planned:
        vert = planned.popleft()
        vert.adjacent.sort(key=lambda node: node.idx)

        for adjacent in vert.adjacent:
            if adjacent.color == WHITE_COLOR:
                adjacent.dist = vert.dist + 1
                adjacent.color = GRAY_COLOR
                planned.append(adjacent)

        vert.color = BLACK_COLOR


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    nodes = [Node(idx, -1, WHITE_COLOR, []) for idx in range(1, n + 1)]

    for _ in range(m):
        i, j = map(lambda a: int(a) - 1, sys.stdin.readline().split())
        node_i = nodes[i]
        node_j = nodes[j]
        node_i.adjacent.append(node_j)
        node_j.adjacent.append(node_i)

    idx1, idx2 = map(lambda a: int(a) - 1, sys.stdin.readline().split())
    dfs(nodes[idx1])
    print(nodes[idx2].dist)


if __name__ == '__main__':
    main()
