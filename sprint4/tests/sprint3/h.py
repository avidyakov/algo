from functools import cmp_to_key


def comparator(first: str, second: str) -> str:
    first_extended = first.ljust(3, first[0])
    second_extended = second.ljust(3, second[0])

    if first_extended == second_extended:
        if first != second:
            return comparator(first[-1], second[-1])
        return 0

    if first_extended < second_extended:
        return -1

    return 1


def get_the_largest_number_from(numbers: list) -> str:
    """
    >>> get_the_largest_number_from(['15', '56', '2'])
    '56215'
    """
    sorted_numbers = sorted(numbers, reverse=True, key=cmp_to_key(comparator))
    return ''.join(sorted_numbers)


def main() -> None:
    input()
    numbers = input().split()
    print(int(get_the_largest_number_from(numbers)))


if __name__ == '__main__':
    main()
