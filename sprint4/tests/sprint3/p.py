def get_max_number_of_blocks(for_sorting: list):
    """
    >>> get_max_number_of_blocks([0, 1, 3, 2])
    3
    >>> get_max_number_of_blocks([1, 0, 2, 3, 4])
    4
    >>> get_max_number_of_blocks([3, 6, 7, 4, 1, 5, 0, 2])
    1
    >>> get_max_number_of_blocks([2, 7, 0, 3, 6, 4, 1, 5, 8, 9])
    3
    """
    acc = 0
    min_ = min(for_sorting)
    max_ = float('-inf')

    for index in range(1, len(for_sorting) + 1):
        current_item = for_sorting[index - 1]
        max_ = max((max_, current_item))

        if min_ not in for_sorting[:index]:
            continue

        slice = for_sorting[index:]
        if slice:
            right_min = min(slice)
        else:
            right_min = float('inf')

        if max_ < right_min:
            acc += 1
            min_ = right_min

    return acc or 1


def main() -> None:
    input()
    numbers = list(map(int, input().split()))
    print(get_max_number_of_blocks(numbers))


if __name__ == '__main__':
    main()
