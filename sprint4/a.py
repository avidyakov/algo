from functools import reduce


def get_polynomial_hash(a, m, string) -> int:
    """
    >>> get_polynomial_hash(123, 100003, 'a')
    97
    >>> get_polynomial_hash(123, 100003, 'hash')
    6080
    >>> get_polynomial_hash(123, 100003, 'HaSH')
    56156
    """
    if not string:
        return 0

    return reduce(lambda i1, i2: (i1 * a + ord(i2)) % m, string[1:], ord(string[0]))


def main() -> None:
    a, m, string = int(input()), int(input()), input()
    print(get_polynomial_hash(a, m, string))


if __name__ == '__main__':
    main()
