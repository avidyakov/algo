def main() -> None:
    n, m = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]

    for edge in range(m):
        i, j = map(int, input().split())
        matrix[i - 1][j - 1] = 1

    for row in matrix:
        print(*row)


if __name__ == '__main__':
    main()
