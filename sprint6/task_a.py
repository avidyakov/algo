def main() -> None:
    n, m = map(int, input().split())
    adjacency = [None]
    adjacency += [None] * n
    edges = (map(int, input().split()) for _ in range(m))

    for edge in edges:
        i, j = edge
        if adjacency[i] is None:
            adjacency[i] = [j]
        else:
            adjacency[i].append(j)

    for idx in range(1, len(adjacency)):
        if adjacency[idx] is None:
            print(0)
        else:
            adjacency[idx].sort()
            print(len(adjacency[idx]), *adjacency[idx])


if __name__ == '__main__':
    main()
