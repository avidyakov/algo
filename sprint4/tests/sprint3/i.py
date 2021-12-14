from collections import Counter


def get_first_k_universities(students: list, k: int) -> list:
    """
    >>> get_first_k_universities([1, 2, 3, 1, 2, 3, 4], 3)
    [1, 2, 3]
    >>> get_first_k_universities([1, 1, 1, 2, 2, 3], 1)
    [1]
    """
    counter = Counter(students).most_common()
    counter.sort(key=lambda i: (-i[1], i[0]))
    return [i[0] for i in counter[:k]]


def main() -> None:
    input()
    students = list(map(int, input().split()))
    k = int(input())
    print(*get_first_k_universities(students, k))


if __name__ == '__main__':
    main()
