import sys
from operator import itemgetter


def get_flower_beds(coordinates: list) -> list:
    """
    >>> get_flower_beds([(7, 8), (7, 8), (2, 3), (6, 10)])
    [[2, 3], [6, 10]]
    >>> get_flower_beds([(2, 3), (5, 6), (3, 4), (3, 4)])
    [[2, 4], [5, 6]]
    """
    sorted_coordinates = sorted(coordinates, key=itemgetter(0))
    united = []

    for start, end in sorted_coordinates:
        if (not united) or (start > united[-1][1]):
            united.append([start, end])
            continue

        if end > united[-1][1]:
            united[-1][1] = end

    return united


def main() -> None:
    n = int(sys.stdin.readline())
    flower_beds = []
    for _ in range(n):
        start, end = sys.stdin.readline().split()
        flower_beds.append((int(start), int(end)))

    for united_flowerbed in get_flower_beds(flower_beds):
        print(*united_flowerbed)


if __name__ == '__main__':
    main()
