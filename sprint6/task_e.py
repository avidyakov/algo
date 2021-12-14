import sys
from dataclasses import dataclass
from itertools import groupby


@dataclass
class Enter:
    __slots__ = ('idx', 'color')
    idx: int
    color: int


def dfs(graph, vertex_idx, occ, component_count):
    stack = [vertex_idx]

    while stack:
        vert = stack.pop()

        if occ[vert].color == -1:
            occ[vert].color = 0
            stack.append(vert)

            outgoing_vertices = graph[vert]
            for vert in outgoing_vertices:
                if occ[vert].color == -1:
                    stack.append(vert)

        elif occ[vert].color == 0:
            occ[vert].color = component_count

    return occ


def get_connectivity_components(graph, n):
    occ = [None, *(Enter(idx=idx, color=-1) for idx in range(1, len(graph)))]
    component_count = 1

    for i in range(1, n + 1):
        if occ[i].color == -1:
            dfs(graph, i, occ, component_count)
            component_count += 1

    return occ


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [None, *([] for _ in range(n))]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    occ = get_connectivity_components(graph, n)
    components = []
    for _, group in groupby(occ[1:], lambda x: x.color):
        components.append([entry.idx for entry in group])

    print(len(components))
    for i in components:
        print(*i)


if __name__ == '__main__':
    main()
