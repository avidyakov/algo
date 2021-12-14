def get_max_perimeter(sides: list) -> int:
    """
    >>> get_max_perimeter([6, 3, 3, 2])
    8
    >>> get_max_perimeter([5, 3, 7, 2, 8, 3])
    20
    """
    sides.sort(reverse=True)

    for right_pointer in range(3, len(sides) + 1):
        left_pointer = right_pointer - 3
        c, b, a = sides[left_pointer:right_pointer]

        if c < a + b:
            return a + b + c


def main() -> None:
    input()
    sides = list(map(int, input().split()))
    print(get_max_perimeter(sides))


if __name__ == '__main__':
    main()
