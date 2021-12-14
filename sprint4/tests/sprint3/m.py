def get_median(south, north) -> int:
    """
    >>> get_median([1, 2], [3, 4])
    2.5
    >>> get_median([0, 0, 0, 1, 3, 3, 5, 10], [4, 4, 5, 7, 7, 7, 8, 9, 9, 10])
    5.0
    """
    half = (len(south) + len(north) + 2) // 2
    south_pointer = north_pointer = 0
    curr = None

    for _ in range(half):
        if south_pointer < len(south):
            south_item = south[south_pointer]
        else:
            south_item = float('inf')

        if north_pointer < len(north):
            north_item = north[north_pointer]
        else:
            north_item = float('inf')

        prev = curr
        curr = min(south_item, north_item)

        if south_item < north_item:
            south_pointer += 1
        else:
            north_pointer += 1

    if (len(south) + len(north)) % 2 == 0:
        return (curr + prev) / 2
    return curr


def main() -> None:
    input(), input()
    south = list(map(int, input().split()))
    north = list(map(int, input().split()))
    print(get_median(south, north))


if __name__ == '__main__':
    main()
