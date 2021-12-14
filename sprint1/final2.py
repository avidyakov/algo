"""ID успешной посылки: 53594958"""

from collections import Counter
from itertools import chain


def max_points(buttons: list, k: int) -> int:
    """ Получить максимальное число баллов, которые могут получить ребята.

    >>> max_points([('1', '2', '3', '1'), ('2', '.', '.', '2'), ('2', '.', '.', '2'), ('2', '.', '.', '2')], 3)
    2
    >>> max_points([('1', '1', '1', '1'), ('9', '9', '9', '9'), ('1', '1', '1', '1'), ('9', '9', '1', '1')], 4)
    1
    >>> max_points([('1', '1', '1', '1'), ('1', '1', '1', '1'), ('1', '1', '1', '1'), ('1', '1', '1', '1')], 4)
    0
    >>> max_points([('1', '9', '9', '9'), ('5', '4', '3', '6'), ('4', '3', '6', '8'), ('1', '7', '1', '2')], 1)
    7
    """
    digit_frequencies = Counter(chain(*buttons))
    all_fingers = k * 2
    points = 0

    for digit, frequency in reversed(digit_frequencies.most_common()):
        if digit == '.':
            continue

        if frequency <= all_fingers:
            points += 1

    return points


def main() -> None:
    k = int(input())
    buttons = [tuple(input()) for _ in range(4)]
    print(max_points(buttons, k))


if __name__ == '__main__':
    main()
