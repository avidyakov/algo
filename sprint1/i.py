from math import log


def is_degree_of_four(number: int) -> bool:
    """Является ли число степенью четверки.

    >>> is_degree_of_four(15)
    False
    >>> is_degree_of_four(16)
    True
    """
    return log(number, 4).is_integer()


def main() -> None:
    number = int(input())
    print(is_degree_of_four(number))


if __name__ == '__main__':
    main()
