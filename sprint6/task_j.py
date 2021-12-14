import sys
from dataclasses import dataclass


@dataclass
class Enter:
    color: str = 'white'


def dfs(graph, vertex_idx, occ, order):
    stack = [vertex_idx]

    while stack:
        vert = stack.pop()

        if occ[vert].color == 'white':
            occ[vert].color = 'gray'
            stack.append(vert)

            outgoing_vertices = graph[vert]
            for vert in outgoing_vertices:
                if occ[vert].color == 'white':
                    stack.append(vert)

        elif occ[vert].color == 'gray':
            occ[vert].color = 'black'
            order.append(vert)

    return occ


def top_sort(graph, n):
    occ = [None, *(Enter() for _ in range(len(graph) - 1))]
    order = []

    for i in range(1, n + 1):
        if occ[i].color == 'white':
            dfs(graph, i, occ, order)

    return order


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [None, *([] for _ in range(n))]
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)

    order = top_sort(graph, n)
    print(*order)


if __name__ == '__main__':
    main()
