def sort_by_counting(values, power: int) -> list:
    """
    >>> sort_by_counting([0, 2, 1, 2, 0, 0, 1], 3)
    [0, 0, 0, 1, 1, 2, 2]
    """
    counted_values = [0] * power
    for value in values:
        counted_values[value] += 1

    sorted_values = []
    for value, count in enumerate(counted_values):
        sorted_values.extend((value, ) * count)

    return sorted_values


def main() -> None:
    input()
    clothes = map(int, input().split())
    print(*sort_by_counting(clothes, 3))


if __name__ == '__main__':
    main()
