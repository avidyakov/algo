import sys
from dataclasses import dataclass


@dataclass
class Enter:
    color: str = 'w'
    start: int = -1
    end: int = -1


def dfs(graph, vertex_idx):
    stack = [vertex_idx]
    occ = [None, *(Enter() for _ in range(len(graph) - 1))]
    time = -1

    while stack:
        vert = stack.pop()

        if occ[vert].color == 'w':
            occ[vert].color = 'g'
            occ[vert].start = time = time + 1
            stack.append(vert)

            outgoing_vertices = graph[vert].copy()
            outgoing_vertices.sort(reverse=True)

            for vert in outgoing_vertices:
                if occ[vert].color == 'w':
                    stack.append(vert)

        elif occ[vert].color == 'g':
            occ[vert].color = 'b'
            occ[vert].end = time = time + 1

    return occ


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [None, *([] for _ in range(n))]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)

    for entry in dfs(graph, 1):
        if entry:
            print(entry.start, entry.end)


if __name__ == '__main__':
    main()
