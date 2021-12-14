"""ID посылки: 60988512

-- ПРИНЦИП РАБОТЫ --
Программа вычисления веса максимального остовного дерева с помощью алгоритма Прима.
Алгоритм реализован на очереди с приоритетами для эффективной работы. Для более удобной работы и не использовал списки
для хранения вершин и для хранения ребер. Я создал два класса Node, Edge для удобной работы.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(∣E∣⋅log∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Для работы алгоритмы мы храним все вершины в памяти и все ребра x2.
Еще у нас есть дополнительное множество для хранения не пройденных вершин, массив для хранения самого остовного дерава,
в котором лежат ребра количеством всех вершин - 1. И доп. массив для хранения ребер количеством всех ребер.

O(∣E∣ + ∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

"""

import typing
from dataclasses import dataclass, field
from heapq import heappush, heappop, heapify
from operator import attrgetter
from sys import stdin


@dataclass(order=True)
class Edge:
    weight: int
    to: 'Node' = field(compare=False)


@dataclass(unsafe_hash=True)
class Node:
    idx: int
    edges: typing.List[Edge] = field(default_factory=list, hash=False)


class DisconnectedGraph(Exception):
    """Граф несвязный"""


def find_mst(nodes: typing.List[Node]):
    not_added = set(nodes[1:])
    edges = nodes[0].edges.copy()
    heapify(edges)
    mst = []

    while not_added and edges:
        edge = heappop(edges)

        if edge.to not in not_added:
            continue

        mst.append(edge)
        not_added.remove(edge.to)

        for edge in edge.to.edges:
            if edge.to in not_added:
                heappush(edges, edge)

    if not_added:
        raise DisconnectedGraph('Исходный граф несвязный')

    return mst


def main() -> None:
    n, m = map(int, stdin.readline().split())
    nodes = [Node(idx) for idx in range(1, n + 1)]

    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        node_u = nodes[u - 1]
        node_v = nodes[v - 1]

        # Складываем отрицательный вес т.к. heapq работает только с мин-кучей.
        node_u.edges.append(Edge(-w, node_v))
        node_v.edges.append(Edge(-w, node_u))

    try:
        mst = find_mst(nodes)
        length = sum(map(attrgetter('weight'), mst))
        print(-length)
    except DisconnectedGraph:
        print('Oops! I did it again')


if __name__ == '__main__':
    main()
