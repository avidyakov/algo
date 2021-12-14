def get_min_difference(islands, k: int) -> int:
    """
    >>> get_min_difference([2, 3, 4], 2)
    1
    >>> get_min_difference([1, 3, 1], 1)
    0
    >>> get_min_difference([1, 3, 5], 3)
    4
    >>> get_min_difference([446681, 809425, 159486, 279231, 354334, 686335, 327432, 568394], 7)
    119745
    """
    differences = []
    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            diff = abs(islands[i] - islands[j])
            differences.append(diff)

    differences.sort()

    return differences[k - 1]


def main() -> None:
    input()
    islands = list(map(int, input().split()))
    k = int(input())
    print(get_min_difference(islands, k))


if __name__ == '__main__':
    main()
