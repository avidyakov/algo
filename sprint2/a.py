def transpose(matrix, total_n, total_m):
    transposed_matrix = [[0 for _ in range(total_n)] for _ in range(total_m)]
    for n in range(total_n):
        for m in range(total_m):
            transposed_matrix[m][n] = matrix[n][m]

    return transposed_matrix


def main():
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(tuple(map(int, input().split())))

    transposed_matrix = transpose(matrix, n, m)
    for line in transposed_matrix:
        print(*line)


if __name__ == '__main__':
    main()
