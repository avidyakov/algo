def get_binary(number: int) -> str:
    """Получить двоичное представление числа.

    >>> get_binary(5)
    '101'
    >>> get_binary(14)
    '1110'
    """
    binary_number = ''
    while number != 1:
        if number % 2 == 0:
            binary_number += '0'
        else:
            binary_number += '1'

        number //= 2

    binary_number += '1'
    return binary_number[::-1]


def main() -> None:
    number = int(input())
    print(get_binary(number))


if __name__ == '__main__':
    main()
