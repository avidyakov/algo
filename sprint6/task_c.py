import sys


def dfs(graph, vertex_idx):
    color = [None]
    color += ['w'] * (len(graph) - 1)
    stack = [vertex_idx]
    bypass = {}

    while stack:
        next_vert = stack.pop()
        if next_vert not in bypass:
            bypass[next_vert] = len(bypass)

        if color[next_vert] == 'w':
            color[next_vert] = 'g'
            stack.append(next_vert)

            outgoing_vertices = graph[next_vert].copy()
            outgoing_vertices.sort(reverse=True)

            for vert in outgoing_vertices:
                if color[vert] == 'w':
                    stack.append(vert)

        elif color[next_vert] == 'g':
            color[next_vert] = 'b'

    return bypass


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    adjacency = [None]
    adjacency += [[] for _ in range(n)]

    for idx in range(m):
        i, j = map(int, sys.stdin.readline().split())
        adjacency[i].append(j)
        adjacency[j].append(i)

    head = int(sys.stdin.readline())
    bypass = dfs(adjacency, head)
    sorted_bypass = map(lambda i: i[0], sorted(bypass.items(), key=lambda key_value: key_value[1]))
    print(*sorted_bypass)


if __name__ == '__main__':
    main()
