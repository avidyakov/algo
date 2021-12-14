"""ID успешной посылки: 53592448"""

from itertools import chain


def get_distances(street: tuple) -> list:
    """ Получить расстояния домов до ближайших пустых участков.

    >>> get_distances([0, 1, 4, 9, 0])
    [0, 1, 2, 1, 0]
    >>> get_distances([0, 7, 9, 4, 8, 20])
    [0, 1, 2, 3, 4, 5]
    >>> get_distances([98, 0, 10, 77, 0, 59, 28, 0, 94])
    [1, 0, 1, 1, 0, 1, 1, 0, 1]
    """
    street_length = len(street)
    distances = [float('inf')] * street_length
    current_distance = float('inf')
    for index in chain(range(street_length), range(-1, -street_length - 1, -1)):
        if street[index] == 0:
            current_distance = 0
        else:
            current_distance += 1

        if current_distance < distances[index]:
            distances[index] = current_distance

    return distances


def main() -> None:
    input()
    street = tuple(map(int, input().split()))
    print(*get_distances(street))


if __name__ == '__main__':
    main()
