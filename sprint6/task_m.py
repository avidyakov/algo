import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    left = []
    right = []

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        left.append(i)
        right.append(j)

    for idx in range(1, m):
        if right[idx] in left or left[idx] in right:
            left[idx], right[idx] = right[idx], left[idx]

    print('YES' if not set(left) & set(right) else 'NO')


if __name__ == '__main__':
    main()
