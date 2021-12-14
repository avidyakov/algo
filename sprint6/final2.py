from sys import stdin
import typing
from dataclasses import dataclass, field
from collections import deque

from icecream import ic

WHITE_COLOR = 'w'
GRAY_COLOR = 'g'
BLACK_COLOR = 'b'


@dataclass
class Edge:
    type: str
    to: 'Node'


@dataclass
class Node:
    idx: int
    color: str = WHITE_COLOR
    route: str = ''
    # routes: typing.List[str] = field(default_factory=list)
    edges: typing.List[Edge] = field(default_factory=list)


def dfs(vert: Node):
    planned = deque((vert, ))
    vert.color = GRAY_COLOR
    visited = []

    while planned:
        vert = planned.popleft()
        visited.append(vert.idx)

        for edge in vert.edges:
            # edge.to.routes.append()
            edge.to.route = vert.route + edge.type

            if edge.to.color == WHITE_COLOR:
                edge.to.color = GRAY_COLOR
                planned.append(edge.to)

        vert.color = BLACK_COLOR

    return visited


def main() -> None:
    n = int(stdin.readline())
    nodes = [Node(idx) for idx in range(1, n + 1)]

    for city_id in range(n):
        roads = stdin.readline().rstrip()

        for next_city, road_type in enumerate(roads, 1):
            road = Edge(road_type, nodes[city_id + next_city])
            nodes[city_id].edges.append(road)

    ic(dfs(nodes[0]))
    ic(nodes)
    # result = is_it_optimal(cities)
    # print('YES' if result else 'NO')


if __name__ == '__main__':
    main()
