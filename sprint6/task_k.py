import typing
from dataclasses import dataclass


@dataclass
class Edge:
    to: 'Node'
    dist: int


@dataclass
class Node:
    idx: int
    dist: int | float = float('inf')
    visited: bool = False
    prev: typing.Optional['Node'] = None


def get_not_visited_vertex(nodes: list) -> Node | None:
    return min(
        filter(lambda node: not node.visited, nodes),
        key=lambda node: node.dist,
        default=None
    )


def relax():
    pass


def dijkstra(nodes):
    while vert := get_not_visited_vertex(nodes):
        vert.visited = True


def main() -> None:
    n, m = map(int, input().split())
    nodes = [Node(idx) for idx in range(1, n + 1)]
    nodes[0].dist = 0

    for _ in range(m):
        i, j, length = map(int, input().split())
        node_i = nodes[i - 1]
        node_j = nodes[j - 1]

    dijkstra(nodes)


if __name__ == '__main__':
    main()
