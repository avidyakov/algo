from itertools import accumulate


def get_gap_len(results: list) -> int:
    """
    >>> get_gap_len([-1, 1])
    2
    >>> get_gap_len([-1, 1, -1])
    2
    >>> get_gap_len([-1, -1, 1, -1, -1, -1, 1, -1, -1, 1])
    4
    """
    max_ = pointer = 0

    while pointer != len(results) and max_ < len(results):
        try:
            idx = len(results[pointer:]) - tuple(accumulate(results[pointer:]))[::-1].index(0)
            if idx > max_:
                max_ = idx
        except ValueError:
            pass

        pointer += 1

    return max_


def main() -> None:
    input()
    results = [int(item) or -1 for item in input().split()]
    print(get_gap_len(results))


if __name__ == '__main__':
    main()
